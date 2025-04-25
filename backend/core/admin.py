import matplotlib
matplotlib.use("Agg")
from django.contrib import admin
from django.utils.html import format_html

from .models import Portfolio, Asset, Position
from django.urls import path, reverse
from django.template.response import TemplateResponse
import matplotlib.pyplot as plt
import io
import base64

class CustomPortfolioAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path("chart/<int:portfolio_id>/", self.admin_site.admin_view(self.chart_view))]
        return my_urls + urls

    def chart_view(self, request, portfolio_id):
        portfolio = Portfolio.objects.get(pk=portfolio_id)
        positions = Position.objects.filter(portfolio=portfolio).select_related("asset")
        data = {}

        for pos in positions:
            type_ = pos.asset.type
            data[type_] = data.get(type_, 0) + (float(pos.quantity) * float(pos.price_at_buy))

        labels = list(data.keys())
        values = list(data.values())
        
        total = sum(values)
        legend_labels = [f"{label}: {round(value/total*100, 2)}% ({int(value)}€)" for label, value in zip(labels, values)]

        fig, ax = plt.subplots(figsize=(6, 6))
        wedges, texts, autotexts = ax.pie(values, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        
        ax.legend(wedges, legend_labels, title="Type d'actifs", loc="center left", bbox_to_anchor=(1, 0.5))

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode("utf-8")
        buf.close()
        plt.close(fig)

        return TemplateResponse(request, "admin/portfolio_chart.html", {
            "chart": img_base64,
            "portfolio": portfolio
        })

    def view_chart_link(self, obj):
        return format_html(
            '<a href="/admin/core/portfolio/chart/{}/">Voir graphique</a>', obj.id
        )

    view_chart_link.short_description = "Répartition graphique"
    list_display = ("name", "type", "view_chart_link")

admin.site.register(Portfolio, CustomPortfolioAdmin)
admin.site.register(Asset)
admin.site.register(Position)

