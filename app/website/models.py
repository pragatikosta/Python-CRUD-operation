from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)  # Corrected 'max_Length' to 'max_length'
    college = models.CharField(max_length=200)  # Corrected 'max_Length' to 'max_length'
    age = models.IntegerField()  # Removed 'max_length' as it's not applicable for IntegerField
    is_active = models.BooleanField(default=False)
 