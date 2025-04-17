from django.http import JsonResponse
from django.db.models import Q
from django.views import View
from django.conf import settings
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Portfolio, Asset, Position
from .serializers import PortfolioSerializer, AssetSerializer, PositionSerializer
from .services.performance import calculate_portfolio_value


# routes
## GET /portfolios/
## POST /portfolios/
## GET /portfolios/{id}/positions/
## POST /positions/
## GET /portfolios/{id}/value/
## UPDATE /portfolios/{id}/positions/{position_id}/


@require_GET
def list_positions(request, portfolio_id=None):
    try:
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)
        positions = Position.objects.filter(portfolio=portfolio).select_related("asset")
        serializer = [PositionSerializer.serialize(pos) for pos in positions]
        return JsonResponse(serializer, safe=False)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)
    

@require_POST
def create_position(request):
    data = request.POST.dict()
    if not all(key in data for key in ['portfolio_id', 'asset_id', 'quantity', 'price_at_buy', 'date']):
        return JsonResponse({"message": _("Missing required fields.")}, status=400)
    pos = Position.objects.create(**data)
    return JsonResponse(PositionSerializer.serialize(pos), status=201)


def update_position(request, portfolio_id, position_id):
    if request.method == 'PUT':
        pos = get_object_or_404(Position, portfolio_id=portfolio_id, id=position_id)
        data = request.POST.dict()
        if not all(key in data for key in ['quantity', 'price_at_buy', 'date']):
            return JsonResponse({"message": _("Missing required fields.")}, status=400)
        pos.quantity = data['quantity']
        pos.price_at_buy = data['price_at_buy']
        pos.date = data['date']
        pos.save()
        return JsonResponse(PositionSerializer.serialize(pos), status=200)
    return JsonResponse({"message": _("Invalid request method.")}, status=405)



class PortfolioListApiView(View):
    @staticmethod
    def get(request):
        portfolios = Portfolio.objects.all()
        serializer = [PortfolioSerializer.serialize(portfolio) for portfolio in portfolios]
        return JsonResponse(serializer, safe=False)
    
    @staticmethod
    def post(request):
        serializer = PortfolioSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@require_GET
def portfolio_value(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    value = calculate_portfolio_value(portfolio)
    
    return JsonResponse({"value": round(value, 2)}, status=200)