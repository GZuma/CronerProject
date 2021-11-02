from django.db import models

# This is the model for the PostgreSQL that mimics the format of the 
# JSON model at https://api.dictionaryapi.dev/api/v2/entries/en/ 

class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    phonetics = models.TextField(default=list)
    meanings = models.TextField(default=list)
    created_in = models.CharField(max_length=50,default="PostgreSQL")
    
    def __str__(self):
        return self.word