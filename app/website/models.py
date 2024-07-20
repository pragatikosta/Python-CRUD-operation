from django.db import models

# Create your models here.
class student(models.model):
    name=models.CharField(max_Length=200)
    college=models.CharField(max_Length=200)
    age=models.IntergerField(max_Length=10)
    is_active=models.BooleanField(default=False)
    


