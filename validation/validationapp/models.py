from django.db import models

# Create your models here.
# validation/models.py
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, ValidationError
from datetime import date

def validate_plate_number(value):
      valid_prefixes = ['IT', 'GR', 'RNP', 'RDF', 'GP']
      if value and not any(value.startswith(prefix) for prefix in valid_prefixes):
        raise ValidationError('Invalid plate number.')

def validate_Mdate(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age > 23:
        raise ValidationError('Participants must be 18 years or older.')

class Vehicle(models.Model):
    
     
     make= models.CharField(max_length=255)
     model = models.CharField(max_length=255)
     plate_number = models.CharField(max_length=20, validators=[validate_plate_number])
     color = models.CharField(max_length=255)
     manufactured_date = models.DateField(validators=[validate_Mdate])
     


def __str__(self):
        return f'{self.make} {self.model} - {self.plate_number}'

def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError('Participants must be 18 years or older.')

def validate_plate_number(value):
    valid_prefixes = ['IT', 'GR', 'RNP', 'RDF', 'GP']
    if value and not any(value.startswith(prefix) for prefix in valid_prefixes):
        raise ValidationError('Invalid plate number.')

def validate_phone_number(value):
    if not value.startswith('+250'):
        raise ValidationError(('Phone number should start with +250'))

class Participant(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
    

    date_of_birth = models.DateField(validators=[validate_age])
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(validators=[RegexValidator(r'@ur\.ac\.rw$')])
    phone = models.CharField(max_length=15, validators=[validate_phone_number],default="")
    reference_number = models.IntegerField(validators=[MinValueValidator(99), MaxValueValidator(999)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
   
    

    def clean(self):
        if not (self.middle_name or self.reference_number):
            raise ValidationError('Either middle name or reference number must be provided.')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
   

