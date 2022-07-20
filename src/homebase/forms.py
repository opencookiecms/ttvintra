
from django.forms import ModelForm, fields
from django import forms
from homebase.models import Userprofile

class userprofileForm(forms.ModelForm):

    class Meta:
        model = Userprofile

        fields = [
            'employeeid',
            'givename',
            'displayname',
            'mailaddress',
            'offid',
            'subid',
            'designation',
            'department',
            'userstatus',
            'supervisor1',
            'supervisor2',
            'supervisor3',
           

        ]