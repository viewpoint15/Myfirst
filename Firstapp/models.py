from django.db import models

# Create your models here.
class Company(models.Model):
    Company_name = models.CharField(max_length=50)
    Ceo = models.CharField(max_length=50)
    Origin = models.CharField(max_length=50)
    Est_Year = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Company_name
    
class Product(models.Model):
    Product_name = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Price = models.IntegerField()
    Seat_Capacity = models.IntegerField()
    Fuel_type = models.CharField(max_length=50)
    Top_Speed = models.IntegerField()
    Milage = models.IntegerField()
    Company = models.ForeignKey(Company,related_name='Compaines',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Product_name