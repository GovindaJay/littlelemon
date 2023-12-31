from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Booking (models.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self):
      return f"{self.name}, {self.No_of_guests}, {self.BookingDate}"

    

class Menu(models.Model):

    title= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    inventory = models.IntegerField(default=0)
    
    def __str__(self):
      return f"{self.title} -- Price ${str(self.price)}"
    
    
    
    
    