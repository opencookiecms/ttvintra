from django import forms
from django.db.models import Q
from trvrequest.models import Travelinfo, AknowlegdeTicket
from homebase.models import Specialuser

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
    projectcode = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project Code / Work Order'}))
    customername = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Name or Company Name'}))
    travelpurpose = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Travel Purpose', 'rows':'4'}))
    destinations = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control form-control-lg form-control', 'type':'text', 'placeholder':'Destination(s)', 'rows':'4'}))
    datearrive = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    timearrive = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    datereturn = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    timereturn  = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

    airlinepreferred = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Airline Preferred'}))
    seatingpreferred = forms.ChoiceField(choices=seeting, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    hotellocation = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Hotel location'}))
    numbernights = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of Nights'}))
    luggageweight = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Weight of luggage (kg)'}))
    luggagereason = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the reason', 'rows':'4'}))


    numbernights = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of Nights'}))
    hotellocation = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Hotel location'}))
    hodapproval = forms.ModelChoiceField(required=False, queryset=Specialuser.objects.filter(Q(position='HOD') | Q(position='Director')), widget=forms.Select(attrs={'class':'form-control'}))
    directorapproval = forms.ModelChoiceField(required=False, queryset=Specialuser.objects.filter(Q(position='Director')), widget=forms.Select(attrs={'class':'form-control'}))
    status = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'class':'form-control','placeholder':'Remarks','value':'New'}))

    
    issuetref = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks','value':'Ticket Reference'}))
    issuetype = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks','value':'Ticket Type'}))
    issuetdate = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks','value':'Ticket Date'}))

    #hodapproval = forms.ModelChoiceField(required=False, queryset=Specialuser.objects.filter(Q(position='HOD') | Q(position='Manager')), widget=forms.Select(attrs={'class':'form-control'}))
    #directorapproval = forms.ModelChoiceField(required=False, queryset=Specialuser.objects.filter(Q(position='Director')), widget=forms.Select(attrs={'class':'form-control'}))
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
            'hotelneeded', 
            'numbernights', 
            'hotellocation', 
            'status', 
            'hodapproval', 
            'hodemail', 
            'directorapproval', 
            'dremail', 
        ]


class TraveleditForm(forms.ModelForm):

    travelpurpose = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Travel Purpose', 'rows':'4'}))
    customername = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks','value':'Ticket Reference'}))
    projectcode = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks','value':'Ticket Reference'}))
    destinations = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks','value':'Ticket Reference'}))
    datereturn = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Travelinfo
        fields = [
           
         
            'travelpurpose',
            'customername', 
            'projectcode',
            'destinations',
            'datereturn', 
         
        ]


class TicketForm(forms.ModelForm):

    transportsw = (
        ('None', 'Select the transport'),
        ('Car', 'Car'),
        ('Bus', 'Bus'),
        ('Flight', 'Flight'),
        ('Train', 'Train'),
    )

    transport = forms.ChoiceField(choices=transportsw, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    issuetref = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reference ticket number'}))
    issuetdate = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    issuelink = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reference ticket number link'}))
    issuefile = forms.FileField(required=False)
    class Meta:
        model = AknowlegdeTicket
        fields = [
            'transport', 
            'issuetref',
            'issuetdate', 
            'issuelink',
            'issuefile', 
            'createby', 
            'issuerelate',
        ]