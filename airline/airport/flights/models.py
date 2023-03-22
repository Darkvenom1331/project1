from django.db import models


class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)
    
    def __str__(self):
       return f"{self.city} ({self.code})"

    

# Create your models here.
class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
       return f"{self.id}:{self.origin} to {self.destination}"
    

# CASCADE means if the referenceing keyword in ariport id deleted ,it also going to delete the keyword in flights
# when ever new changes made in models.py you have to create a new migrations by python manage.py makemigrations

class Passenger(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")
     
    def __str__(self):
        return f"{self.first} {self.last}"