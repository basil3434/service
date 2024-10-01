from django.db import models

# Create your models here.


class Customer(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    vehicle_number=models.CharField(max_length=200)
    running_kilometer=models.IntegerField()
    status_options=[
        ("Pending","Pending"),
        ("In Progress","In Progress"),
        ("Completed","Completed")
    ]
    work_status=models.CharField(max_length=200,choices=status_options)

class Work(models.Model):
    customer_object=models.ForeignKey(Customer,on_delete=models.CASCADE)
    description=models.TextField(max_length=200)
    amount=models.FloatField()