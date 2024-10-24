from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject=models.TextField()
    email = models.EmailField(max_length=255)
    created_date =models.DateField(auto_now_add = True)
    update_date = models.DateField(auto_now =True)
    message=models.TextField()

    class Meta:
        ordering = ['created_date']

class Newsletter(models.Model):
    email=models.EmailField(max_length=255)
