from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.forms import ModelForm
import os
from uuid import uuid4

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

TYPE_SELECT = (
        ('0', 'No'),
        ('1', 'Yes'),
    )

APPETITE_CHANGE = (
    ('Increased', 'Increased'),
    ('Decreased','Decreased'),
    ('No Change','No Change')
)

DRINKING_MORE_WATER = (
    ('Yes','Yes'),
    ('No','No'),
    ('No Change','No Change')
)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="user"
    )
    firstname = models.CharField(max_length=50, blank=False, verbose_name="FirstName")
    midname = models.CharField(max_length=50, blank=True, verbose_name="MidName")
    lastname = models.CharField(max_length=50, blank=False, verbose_name="LastName")

    def userphoto_path(instance, filename):
        upload_to = 'images/enrolleduser'
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
        return os.path.join(upload_to, filename)

    usertpic = models.ImageField(default='Default.jpg', upload_to=userphoto_path, verbose_name="User Picture",
                                  max_length=255, blank=True)
    address = models.TextField(verbose_name="Address", default='')
    streetaddress = models.CharField(max_length=100, verbose_name="Street Address", default='')
    addressline2 = models.TextField(blank=True, verbose_name="AddressLine2")
    city = models.CharField(max_length=100, verbose_name="City", default='')
    state = models.CharField(max_length=200, verbose_name="State", blank=True)
    zip = models.CharField(max_length=20, verbose_name="Zip", blank=False)
    homephone = models.CharField(max_length=30, blank=True, verbose_name="Home Phone")
    workphone = models.CharField(max_length=30, blank=True, verbose_name='Work Phone')
    cellphone = models.CharField(max_length=30, blank=True, verbose_name='Cell Number')
    email = models.EmailField(blank=False, default='', verbose_name='Email')
    employer = models.CharField(max_length=100, blank=True, verbose_name='Employer')
    hearaboutus = models.CharField(max_length=30, choices=ABOUT_CHOICES, default='Google', verbose_name='Heard From')
    refvet = models.CharField(max_length=100, blank=True, verbose_name='Referring Veterinarian')
    familyvet = models.CharField(max_length=100, blank=True, verbose_name='Family Veterinarian')
    created_date = models.DateTimeField(default=now, blank=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Pet(models.Model):
    petuser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="petuser",
        verbose_name="user"
    )
    petname = models.CharField(max_length=100, verbose_name="Pet Name")

    def petphoto_path(instance, filename):
        upload_to = 'images/pet'
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
        return os.path.join(upload_to, filename)

    petpic = models.ImageField(default='Default.jpg', verbose_name="Pet Picture", upload_to=petphoto_path, blank=True)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='Canine', verbose_name="Species")
    sex = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male', verbose_name="Gender")
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    initproblem = models.TextField(verbose_name="Initial Problem", blank=True)
    picauthorization = models.BooleanField(default=False, verbose_name="Picture Authorization")
    created_date = models.DateTimeField(default=now, editable=False, blank=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.petname

class Owner(models.Model):
    petowner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="petowner",
        verbose_name="user"
    )
    ownername = models.CharField(max_length=100, verbose_name='Owner Name')
    created_date = models.DateTimeField(default=now, blank=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.ownername

class MedicalHistory(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    duration_pet_owned = models.CharField(max_length=100, blank=False, default='0', verbose_name="How long have you owned your pet?")
    pet_obtained = models.CharField(max_length=100, blank=False ,verbose_name='Where was your pet obtained?')
    pet_allowed_outside = models.CharField(max_length=10, choices=TYPE_SELECT, default='Yes', verbose_name='Does your pet ever go outside?')
    pet_allowed_roam_free = models.CharField(max_length=10, choices=TYPE_SELECT, default='Yes', verbose_name='Is your pet allowed to roam free?')
    board_hosp_animal_shelter = models.CharField(max_length=10, choices=TYPE_SELECT, default='Yes',
                                                 verbose_name='Has your pet been boarded, hospitalized or at the animal shelter recently?')
    any_other_household = models.CharField(max_length=10, choices=TYPE_SELECT, default='Yes', verbose_name='Are there any other animals in your household?')

class VaccinationHistory(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    dog_dist_parvo_corona = models.CharField(max_length=50, blank=True, verbose_name='Dog:Distemper/Parvo/Corona')
    dog_leptospirosis = models.CharField(max_length=50, blank=True, verbose_name='Dog:Leptospirosis?')
    dog_rabies = models.CharField(max_length=50, blank=True, verbose_name='Dog:Rabies?')
    dog_bordatella = models.CharField(max_length=50, blank=True, verbose_name='Dog:Bordatella?')
    cat_panleukopenia_rhinotracheitis_calicivirus = models.CharField(max_length=50, blank=True,
                                                                     verbose_name='Cat:Panleukopenia/Rhinotracheitis/Calicivirus?')
    cat_rabies = models.CharField(max_length=50, blank=True, verbose_name='Cat:Rabies?')
    cat_feline_leukemia_virus = models.CharField(max_length=50, blank=True, verbose_name='Cat: Feline Leukemia Virus (FeLV)?')
    cat_feline_immunodeficiency_virus = models.CharField(max_length=50, blank=True, verbose_name='Cat: Feline Immunodeficiency Virus (FIV, feline, AIDS)?')
    treated_any_medical_problems = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                    verbose_name='Prior to this illness, has your pet been treated for any medical problems?')
    age_when_surgery_performed = models.CharField(max_length=10, blank=True,
                                                  verbose_name='If your pet is neutered/spayed, what was his/her age when this surgery was performed?')
    any_other_surgery = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                         verbose_name='Has your pet undergone any other surgery?')
    female_any_litters = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                          verbose_name='If your pet is female has she had any litters?')
    female_last_heat_cycle = models.CharField(max_length=50, blank=True,
                                              verbose_name='If your pet is female and not spayed, when was her last heat cycle?')
    abnormal_vaginal_discharge = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='If your pet is female, has there been any abnormal vaginal discharge?')
    medication_for_heatwork_disease = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet taking medicine to prevent heatwork disease?')
    medication_for_fleas = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet now taking medicine to prevent fleas?')
    medication_for_ticks = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet taking medicine to prevent ticks?')
    traveled_out_of_mexico = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet traveled out of New Mexico?')
    normally_eat = models.CharField(max_length=100 , blank=False, verbose_name='What does your pet eat normally?')
    howmuch_howoften_eat = models.CharField(max_length=100, blank=False, verbose_name='Approximately how much and how often does your pet eat?')
    ever_fed_table_scraps = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet ever fed table scraps?')
    appetite_increased_decreased = models.CharField(max_length=10, choices=APPETITE_CHANGE, default='Increased',
                                                  verbose_name='Has your pet\'s diet increased decreased recently?')
    drinking_more_water = models.CharField(max_length=10, choices=DRINKING_MORE_WATER, default='No',
                                                  verbose_name='Is your pet drinking more water than usual?')
    urinating_more_than_usual = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet urinating more than usual?')
    straining_to_urinate = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet straining to urinate?')
    blood_or_discolouration_urine = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is there any blood or discoloration of your pet\'s urine?')
    vomiting = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet been vomiting?')
    change_in_bowl_moments = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Have there been any recent changes in the frequency, amount or color of your pet\'s bowel movements?')
    straining_to_defecate = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Is your pet straining to defecate?')
    itching_or_scratching = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet been itching or scratching?')
    discharge_from_eyes_nose = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet had any discharge from eyes or nose?')
    sneezing_excessively = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet been sneezing excessively?')
    coughing_difficulty_breating = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet been coughing or showing difficulty breathing?')
    seizures_or_convulsions = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet had any seizures or convulsions?')
    change_attitude_behavior = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet shown any change in attitude or behavior?')

    lost_stamina_recently = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet lost stamina recently?')
    walk_changed = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet\'s walk changed?')
    noticed_swelling_or_masses = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Have you noticed any swelling or masses?')
    unusual_reaction_to_medications = models.CharField(max_length=10, choices=TYPE_SELECT, default='No',
                                                  verbose_name='Has your pet had unusual/unexpected reactions to medications?')
    current_medication  = models.TextField(blank=False, verbose_name='What medications is your pet currently receiving?')
    primary_concern = models.TextField(blank=False, verbose_name='What is your primary concern about your pet?')
    def petfile_path(instance, filename):
        upload_to = 'files/pet'
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
        return os.path.join(upload_to, filename)

    #petpic = models.ImageField(blank=True, verbose_name="Pet Picture", upload_to=petfile_path)
    vaccination_history = models.FileField(blank=True, verbose_name='Vaccination History File', upload_to=petfile_path)

class PrivateMessages(models.Model):
    msg_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="messagesender",
        verbose_name="From"
    )
    msg_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="messagereceiver",
        verbose_name="Client"
    )
    subject = models.TextField(blank=False, verbose_name='Subject')
    message = models.TextField(blank=False, verbose_name='Message')
