import imp
from django import forms
from django.db import models
from django.conf import settings
from django.db.models import Q
from trvrequest.models import Travelinfo, AknowlegdeTicket

from intra.settings import DATE_INPUT_FORMAT

class TravelRequestForm(forms.ModelForm):

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    seeting = (
        ('Either', 'Either'),
        ('Window', 'Window'),
        ('Aisle', 'Aisle')
    )


    date = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'DD/MM/YYYY'}))
    projectcode = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project Code'}))
    travelpurpose = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Travel Purpose', 'rows':'4'}))
    destinations = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control form-control-lg form-control-solid', 'type':'text', 'placeholder':'Destination(s)', 'rows':'4'}))
    datearrive = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    timearrive = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    datereturn = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    timereturn  = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

    airlinepreferred = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Airline Preferred'}))
    seatingpreferred = forms.ChoiceField(choices=seeting, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    luggageneeded = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, required=False, widget=forms.Select(attrs={'class':'form-control','placholder':'Luggage Needed'}))
    luggageweight = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Weight of luggage (kg)'}))
    luggagereason = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the reason', 'rows':'4'}))
    class Meta:
        model = Travelinfo
        fields = [
            'offid',
            'companyname',
            'name',
            'emailname', 
            'date',
            'travelpurpose',
            'customername', 
            'projectcode',
            'destinations',
            'datearrive', 
            'datereturn', 
            'timearrive', 
            'timereturn', 
            'transport', 
            'airlinepreferred', 
            'seatingpreferred', 
            'luggageneeded', 
            'luggageweight', 
            'luggagereason', 
            'numbernights', 
            'hotellocation', 
            'status', 
            'hodapproval', 
            'hodemail', 
            'directorapproval', 
            'dremail', 
        ]