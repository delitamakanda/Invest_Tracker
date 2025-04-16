from django.urls import path
from .views import PortfolioListApiView

urlpatterns = [
    path('portfolios/', PortfolioListApiView.as_view(), name='portfolio_list'),
]