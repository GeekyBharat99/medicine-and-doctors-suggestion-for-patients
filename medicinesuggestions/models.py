from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Doctors(models.Model):
    Name = models.CharField(max_length=100, null=True,blank=True)
    specialist = models.CharField(max_length=100, null=True,blank=True)
    number = models.IntegerField(null=True, blank=True)
    hospital_name = models.CharField(max_length=200,null=True,blank=True)
    address = models.TextField(max_length=400,blank=True,null=True)

    def __str__(self):
        return self.Name


class Medicines(models.Model):
    Name = models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return self.Name

class Disease(models.Model):
    Name = models.CharField(max_length=120,null=True,blank=True)
    Specialist_Doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True, blank=True)
    Suggested_medicine = models.ForeignKey(Medicines, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Name



class Contactus(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    message = models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):

        return self.name

