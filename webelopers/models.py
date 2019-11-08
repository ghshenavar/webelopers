from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	document = models.FileField(upload_to='media/')

# Create your models here.
DAYS_OF_WEEK = (
    (0, 'Saturday'),
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
)


class Course(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(max_length=1, choices=DAYS_OF_WEEK)
    second_day = models.IntegerField(max_length=1, choices=DAYS_OF_WEEK)