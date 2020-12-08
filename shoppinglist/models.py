from django.db import models

# Create your models here.
class Shoppinglist(models.Model):  
    name = models.CharField(max_length=100)  
    qty = models.IntegerField()  
    price = models.FloatField(max_length=15) 
    boolkg = models.BooleanField() 
    class Meta:  
        db_table = "shoppinglist"  