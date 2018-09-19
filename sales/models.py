from django.db import models
from accounts.models import User
# Create your models here.
class Customer(models.Model):
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.id.first_name

class Agent(models.Model):
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.id.first_name

class Vehicle(models.Model):
    plate_no = models.CharField(max_length=50)
    model_type = models.CharField(max_length=50)
    model_name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.model_name

class Sale(models.Model):
    vehicle_id = models.ForeignKey(Vehicle)
    customer_id = models.ForeignKey(Customer)
    agent_id = models.ForeignKey(Agent)

    def __str__(self):
        return self.customer_id.first_name
