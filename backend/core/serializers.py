from django.forms.models import model_to_dict

class PortfolioSerializer:
    @staticmethod
    def serialize(instance):
        return model_to_dict(instance, fields=['id', 'type', 'name'])
    

class AssetSerializer:
    @staticmethod
    def serialize(instance):
        return model_to_dict(instance, fields=['id', 'name', 'ticker', 'type'])
    
class PositionSerializer:
    @staticmethod
    def serialize(instance):
        return model_to_dict(instance, fields=['id', 'portfolio', 'asset', 'quantity', 'price_at_buy', 'date'])

