from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)  # Added max_length
    message = models.TextField()