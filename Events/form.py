from django import forms
from django.db import models


class FormEmailSubscriber(forms.Form):
    subscriber_mail = forms.EmailField(max_length=30, label="Email")


class FormApplyCandidates(forms.Form):
    full_name = forms.CharField(max_length=50, label="Full Name", required=True)
    gender = forms.CharField(widget=forms.Select(choices=('Male', 'Female', 'Others')))
    email = forms.EmailField(max_length=40, label="Email", required=True,
                             help_text="Enter a valid email, it will used to contact you")
    dob = forms.DateField(required=True)
    state = forms.CharField(max_length=30, label="State", required=True)
    college_name = forms.CharField(max_length=200, label="College", required=True,
                                   help_text="College Name must be under 100 characters")
    degree_level = forms.CharField(widget=forms.Select(choices=('Some School', 'Bachelor Degree', 'Master Degree')))
    degree_program = forms.CharField(max_length=50, required=True, help_text="Branch you study right now")
    graduation_date = forms.DateField(required=True)
    video = forms.URLField()
