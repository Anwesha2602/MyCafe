from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError('Date cannot be in the past.')
    
    
def validate_phone_number(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Phone number must be 10 numeric digits.')

def validate_time(value):
    current_time = timezone.now().time()
    if value < current_time:
        raise ValidationError("Please select a current or future time.") 
    
def validate_table(value):
    if value<0:
        raise ValidationError("Please select a table.") 
    
class Menu_items(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    desc=models.TextField()
    img=models.URLField(blank=True)
    def __str__(self):
        return self.name

class Logger(models.Model):
    name=models.CharField(max_length=50)
    time=models.TimeField(validators=[validate_time])
    table=models.PositiveIntegerField(validators=[validate_table])
    email=models.EmailField(help_text='abc@gmail.com')
    phone_no=models.CharField(max_length=10, validators=[validate_phone_number])
    date=models.DateField(validators=[validate_future_date])
    def __str__(self):
        return self.name





# Create your models here.
