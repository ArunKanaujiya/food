from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    Company_Name=models.CharField(max_length=100)
    Company_logo=models.FileField(null=True,blank=True)
    Company_city=models.CharField(max_length=100)

    def __str__(self):
        return self.Company_Name
    def get_absolute_url(self):
        return reverse('retrive',kwargs={'id':self.id})