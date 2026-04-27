from django.db import models
from django.contrib.auth.models import User, auth
from django_resized import ResizedImageField

# Create your models here.

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # link to default auth table
    passport = ResizedImageField(size=[320,300], upload_to="passport/", null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    dob = models.DateField(null=True, blank=True) # Date of Birth
    ph = models.CharField(max_length=500, null=True, blank=True)
    gender= models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, null=True, blank=True)
    password = models.CharField(max_length=500, null=True, blank=True)
    is_superuser = models.CharField(max_length=500, null=True, blank=True) # if admin(1) or user(0)
    reset = models.CharField(max_length=500, null=True, blank=True) # reset token
    payments = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True) # blocked or non blocked users
    subject = models.CharField(max_length=500, null=True, blank=True)
    
    class Meta: # Class Meta are variables used to manage your table
        managed = True # Django should manage your table
        db_table = 'signup' # define your table name here