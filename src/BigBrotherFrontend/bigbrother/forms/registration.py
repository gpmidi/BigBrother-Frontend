'''
Created on Feb 26, 2011

@author: gpmidi
'''

from django.forms import ModelForm, Form
from BigBrotherFrontend.bigbrother.models import *
from django import forms
from django.core import validators

def isValidUsername(field_data):
    try:
        User.objects.get(username = field_data)
    except User.DoesNotExist:
        return
    raise validators.ValidationError('The username "%s" is already taken.' % field_data)

class RegistrationForm(Form):
    username = forms.CharField(
                               required = True,
                               label = 'Username',
                               help_text = 'The username you want',
                               validators = [
                                             isValidUsername,
                                             validators.MaxLengthValidator(32),
                                             validators.MinLengthValidator(3),
                                             ],
                               )
    email = forms.EmailField(
                             required = True,
                             label = 'Email',
                             help_text = 'Your email address',
                             )
    password1 = forms.CharField(
                               required = True,
                               label = 'Password',
                               help_text = 'The password you want to use to login to the site',
                               validators = [
                                             validators.MaxLengthValidator(32),
                                             validators.MinLengthValidator(7),
                                             ],
                               widget = forms.PasswordInput,
                               )
    password2 = forms.CharField(
                               required = True,
                               label = 'Password (Again)',
                               help_text = 'Re-enter your password',
                               validators = [
                                             validators.MaxLengthValidator(32),
                                             validators.MinLengthValidator(7),
                                             ],
                               widget = forms.PasswordInput,
                               )
