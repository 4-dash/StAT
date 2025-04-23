from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model) :
    '''
    Models a student attending the course
    '''
    firstname = models.CharField(max_length=255, verbose_name="First Name")
    surname = models.CharField(max_length=255, verbose_name="Surname")
    attendence_count = models.IntegerField(verbose_name="Attendence Count", default=0, blank=True, validators=[MinValueValidator(0, "Min attendence is 0")])
  