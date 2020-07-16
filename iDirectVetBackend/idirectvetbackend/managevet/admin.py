from django.contrib import admin
from .models import Profile, Pet, Owner, MedicalHistory, VaccinationHistory, PrivateMessages
from django.contrib import admin  # added for changing the site header, title and index

admin.site.site_title = "iDirectVet"  # added
admin.site.site_header = "iDirectVet"  # added
admin.site.index_title = "VetManagement"  # added
# Register your models here.

admin.site.register(Profile)
admin.site.register(Pet)
admin.site.register(Owner)
admin.site.register(MedicalHistory)
admin.site.register(VaccinationHistory)
admin.site.register(PrivateMessages)