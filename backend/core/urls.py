from django.urls import path
from .views import export_positions_to_csv, PortfolioListApiView, list_positions, create_position, update_position, portfolio_value, health_check

urlpatterns = [
    path('portfolios/', PortfolioListApiView.as_view(), name='portfolio_list'),
    path('portfolios/<int:portfolio_id>/positions/', list_positions, name='position_list'),
    path('portfolios/<int:portfolio_id>/value/', portfolio_value, name='portfolio_value'),
    path('positions/', create_position, name='position_create'),
    path('portfolios/<int:portfolio_id>/positions/<int:position_id>/', update_position, name='position_update'),
    path('positions/export/', export_positions_to_csv, name='position_export'),
    path('health/', health_check, name='health'),
]