from django.db import models

# Fields to be created 
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True) #optional message input
    created_at = models.DateTimeField(auto_now_add=True) #add Date automatically
