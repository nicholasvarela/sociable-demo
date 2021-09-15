from django.db import models

# Create your models here.

class Tweet(models.Model):
    date = models.DateTimeField(auto_now_add = True, null = True)
    text = models.CharField(max_length=280, null = True)
    link = models.CharField(max_length=280, null = True)
    score = models.DecimalField( max_digits=5, decimal_places=2,blank = True,null = True)

    def __str__(self):
        return self.text

class Handle(models.Model):
    at = models.CharField(max_length=280, null = True)
    
    def __str__(self):
        return self.at
        