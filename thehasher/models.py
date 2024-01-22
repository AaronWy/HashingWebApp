from django.db import models

# Create your models here.

class HashFromUser(models.Model): 
    hashText = models.CharField(max_length=200)
    hashType = models.CharField(max_length=200)
    
class HashCatMode(models.Model): 
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)

    def __str__(self): 
        return f"{self.name},{self.Category}"