from django.db import models
from accounts.models.user import User
from accounts.models.country import Country


class Customer(models.Model):
    SURNAME = (('Kaushik','Kaushik'), ('Kumar','Kumar'), ('Choudhary','Choudhary'), 
               ('Gupta','Gupta'), ('Guar','Guar'))
    

    GENDER = (('Male','Male'), ('Female','Female'))

    surname = models.CharField(max_length=100, blank=True, null=True, choices= SURNAME)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.ForeignKey(Country, on_delete= models.CASCADE, related_name='nationality', null=True, blank=True)
    sex = models.CharField(max_length=50, blank=True, null=True, choices= GENDER)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE)