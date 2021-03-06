from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
      
    def __str__(self):
        return self.title

class Product(models.Model):
    product_list = models.CharField(max_length=200)
    product_detail = models.BooleanField(default=False, blank=True, null=True)
    product_create = models.BooleanField(default= False, blank=True, null=True)
    product_delete = models.BooleanField(default= True, blank=True, null= True)
      
    def __str__(self):
        return self.title

        
    # "List": "/product-list/",
    # "Detail View": "/product-detail/<str:pk>/",
    # "Create": "/product-update/<str:pk>/",
    # "Delete": "/product-delete/<str:pk>/"        