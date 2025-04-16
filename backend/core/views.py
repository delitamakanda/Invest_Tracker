from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Asset, Position
from .serializers import PortfolioSerializer, AssetSerializer, PositionSerializer

# routes
## GET /portfolios/
## POST /portfolios/
## GET /portfolios/{id}/positions/
## POST /positions/
## GET /portfolios/{id}/value/
## UPDATE /portfolios/{id}/positions/{position_id}/


class PortfolioListApiView(View):
    @staticmethod
    def get(request):
        portfolios = Portfolio.objects.all()
        serializer = [PortfolioSerializer.serialize(portfolio) for portfolio in portfolios]
        return JsonResponse(serializer, safe=False)