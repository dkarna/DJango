from random import random
from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import os.path

# Create your models here.
GENDER_CHOICES = (('Male', 'Male'),
                  ('Female', 'Female'),
                  ('Male Neutered', 'Male Neutered'),
                  ('Female Spayed', 'Female Spayed'),
                  )

SPECIES_CHOICES = (
    ('Canine', 'Canine'),
    ('Feline', 'Feline'),
    ('Other', 'Other')
)

ABOUT_CHOICES = (
    ('Google', 'Google'),
    ('Yellow Pages', 'Yellow Pages'),
    ('Walk-in', 'Walk-in'),
    ('Other', 'Other')
)

# VetClient creation form
class VetClient(models.Model):
    firstname = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
    midname = models.CharField(max_length=50, blank=True, verbose_name="MidName")
    lastname = models.CharField(max_length=50, blank=False, verbose_name="LastName")
    def photo_path(instance, filename):
        upload_to = 'images/client'
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
        return os.path.join(upload_to, filename)

    clientpic = models.ImageField(default='Default.jpg', upload_to= photo_path, verbose_name="Client Picture", max_length=255)
    address = models.TextField(verbose_name="Address")
    streetaddress = models.CharField(max_length=100, verbose_name="Street Address")
    addressline2 = models.TextField(blank=True, verbose_name="AddressLine2")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=200, verbose_name="State", blank=True)
    zip = models.CharField(max_length=20, verbose_name="Zip", blank=False)
    homephone = models.CharField(max_length=30, blank=True, verbose_name="Home Phone")
    workphone = models.CharField(max_length=30, blank=True)
    cellphone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=False)
    employer = models.CharField(max_length=100, blank=True)
    hearaboutus = models.CharField(max_length=30, choices=ABOUT_CHOICES, default='Google')
    refvet = models.CharField(max_length=100, blank=True)
    familyvet = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

#ClientOwner model for database table
class VetClientOwner(models.Model):
    client = models.ForeignKey('VetClient', on_delete=models.CASCADE, related_name='owners')
    ownername = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ownername

# VetPet model for database table
class VetPet(models.Model):
    vet_user = models.ForeignKey('VetClient', on_delete=models.CASCADE,verbose_name="Client", related_name='pets')
    petname = models.CharField(max_length=100,verbose_name="Pet Name")
    def photo_path(instance, filename):
        upload_to = 'images/pet'
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
        return os.path.join(upload_to, filename)
    petpic = models.ImageField(default='Default.jpg', verbose_name="Pet Picture", upload_to=photo_path)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='Canine', verbose_name="Species")
    sex = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male', verbose_name="Gender")
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    initproblem = models.TextField(verbose_name="Initial Problem")
    picauthorization = models.BooleanField(default=False, verbose_name="Picture Authorization")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.petname

