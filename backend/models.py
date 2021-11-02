from django.db import models

class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    phonetics = models.TextField(default=list)
    meanings = models.TextField(default=list)
    created_in = models.CharField(max_length=50,default="PostgreSQL")
    
    def __str__(self):
        return self.word