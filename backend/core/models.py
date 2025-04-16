from django.db import models

class Portfolio(models.Model):
    TYPE_CHOICES = [
        ('CTO', 'Compte-titres ordinaire'),
        ('PEA', 'Plan d\'Épargne en Actions'),
        ('AV', 'Assurance Vie'),
        ('CP', 'Compte Courant'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    

class Asset(models.Model):
    SYMBOL_TYPE_CHOICES = [
        ('ACTION', 'Action'),
        ('ETF', 'ETF'),
        ('OPC', 'OPCVM'),
        ('CASH', 'Liquidité'),
        ('CRYPTO', 'Cryptocurrency'),
    ]
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, choices=SYMBOL_TYPE_CHOICES)
    
    def __str__(self):
        return self.name
    
    
class Position(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='positions')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    price_at_buy = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.quantity} x {self.asset.name} @ {self.price_at_buy}€"
    
    @property
    def total_cost(self):
        return self.quantity * self.price_at_buy