from django.db import models


class Profile(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	document = models.FileField(upload_to='media/')

# Create your models here.
