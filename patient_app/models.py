from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    aadhar=models.IntegerField()
    address=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    email=models.EmailField()

    def __str__(self):
        return self.name