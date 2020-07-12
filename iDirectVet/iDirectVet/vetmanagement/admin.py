from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(VetClient)
admin.site.register(VetPet)
admin.site.register(VetClientOwner)