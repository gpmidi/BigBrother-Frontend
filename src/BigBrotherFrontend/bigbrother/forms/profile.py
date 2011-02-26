'''
Created on Feb 26, 2011

@author: gpmidi
'''
from django.forms import ModelForm, Form
from BigBrotherFrontend.bigbrother.models import *
from django import forms

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile #@UndefinedVariable
        
    first_name = forms.CharField(
                                 max_length = 255,
                                 min_length = 0,
                                 required = False,
                                 label = "First Name",
                                 help_text = "Your first name (optional)",
                                 )
        
    last_name = forms.CharField(
                                 max_length = 255,
                                 min_length = 0,
                                 required = False,
                                 label = "Last Name",
                                 help_text = "Your last name (very optional)",
                                 )

    email = forms.EmailField(
                             max_length = 75,
                             min_length = 0,
                             required = False,
                             label = "Email Address",
                             help_text = "Your email address",
                             )
