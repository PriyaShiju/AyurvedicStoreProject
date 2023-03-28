from django.db import models

# Create your models here.
class feedback(models.Model):
    submitter=models.CharField(max_length=100)
    body=models.CharField(max_length=1000)
    createdon=models.DateTimeField(auto_now_add=True)
    
