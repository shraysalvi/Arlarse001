from django import forms
from django.db import models


class EmailSubscriberForm(models.Model):
    id = models.AutoField(primary_key=True)
    subscriber_mail = models.EmailField()


class ApplyCandidates(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    state = models.CharField(max_length=20)
    college_name = models.CharField(max_length=200)
    degree_level = models.CharField(max_length=10)
    degree_program = models.CharField(max_length=50)
    graduation_date = models.DateField()
    video = models.URLField()
