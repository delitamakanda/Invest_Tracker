from django.urls import path
from .views import PortfolioListApiView, list_positions, create_position, update_position, portfolio_value

urlpatterns = [
    path('portfolios/', PortfolioListApiView.as_view(), name='portfolio_list'),
    path('portfolios/<int:portfolio_id>/positions/', list_positions, name='position_list'),
    path('portfolios/<int:portfolio_id>/value/', portfolio_value, name='portfolio_value'),
    path('positions/', create_position, name='position_create'),
    path('portfolios/<int:portfolio_id>/positions/<int:position_id>/', update_position, name='position_update'),  # TODO: add PUT method for updating positions.
]