from django.db import models

class House(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField()
    street_name = models.TextField()
    city = models.TextField()
    postal_code = models.TextField()
    
    def __str__(self):
        return self.number
    
    
class HousePurchase(models.Model):
    BUNGALOW = "bungalow"
    DUPLEX = "duplex"
    
    HOUSE_TYPE_CHOICES = (
        (BUNGALOW, BUNGALOW),
        (DUPLEX, DUPLEX),
    )
    
    id = models.AutoField(primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    home_type = models.TextField(choices=HOUSE_TYPE_CHOICES)
    date_of_purchase = models.DateField(auto_now_add=True)