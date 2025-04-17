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
        return {
            'id': instance.id,
            'asset': instance.asset.name,
            'ticker': instance.asset.ticker,
            'quantity': float(instance.quantity),
            'price_at_buy': float(instance.price_at_buy),
            'date': instance.date.isoformat() if instance.date else None,
        }

