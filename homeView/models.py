from django.db import models

# Create your models here.
class Scripts(models.Model):
    scriptName = models.CharField(max_length=50)
    scriptDescription = models.CharField(max_length=500)

    