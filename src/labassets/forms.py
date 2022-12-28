from django import forms
from labassets.models import Camera,Lens



class CameraForm(forms.ModelForm):


    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    isomark = (
        ('', 'Please choose'),
        ('Color', 'Color'),
        ('Mono', 'Not-Mono'),
        ('N/A', 'N/A')
    )

    mounting = (
        ('', 'Please choose'),
        ('C-Mount', 'C-Mount'),
        ('C/F Mount', 'C/F Mount'),
        ('F-Mount', 'F-Mount'),
        ('F(Nikon),T2/M42 x 1 Mount Adapter', 'F(Nikon),T2/M42 x 1 Mount Adapter'),
        ('M58x0.75 Mount Adapter', 'M58x0.75 Mount Adapter'),
        ('M72 Mount', 'M72 Mount'),
        ('Adapter Required', 'Adapter Required'),
    )
    
    cameramodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Camera Name / Module'}))
    assetno =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset Number'}))
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    location  =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item location'}))
    typeitem = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type of the item'})) 
    resolution =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pixel Resolution'}))
    isomark = forms.ChoiceField(choices=isomark, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    mountingtype  = forms.ChoiceField(choices=mounting, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    interfacetype = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Camera Interfaces'})) 
    itempic = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status  = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))


    class Meta:
        model = Camera
        fields = [
            'cameramodule',
            'assetno', 
            'itemdesc' ,
            'location',  
            'typeitem', 
            'resolution', 
            'isomark', 
            'mountingtype',
            'interfacetype',
            'itempic',  
            'attachment', 
            'status', 
            'createby', 
        ]

class LensForms(forms.ModelForm):

    mounting = (
        ('', 'Please choose'),
        ('C-Mount', 'C-Mount'),
        ('C/F Mount', 'C/F Mount'),
        ('F-Mount', 'F-Mount'),
        ('F(Nikon),T2/M42 x 1 Mount Adapter', 'F(Nikon),T2/M42 x 1 Mount Adapter'),
        ('M58x0.75 Mount Adapter', 'M58x0.75 Mount Adapter'),
        ('M72 Mount', 'M72 Mount'),
        ('Adapter Required', 'Adapter Required'),
    )

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )



    lensemodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Camera Name / Module'}))
    assetno  =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset Number'}))
    location =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item location'}))
    typeitem = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type of the item'}))
    focallength  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Focal Length'}))
    mountingtype  = forms.ChoiceField(choices=mounting, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    itemdesc   =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    itempic = forms.FileField(required=False)
    attachment  = forms.FileField(required=False) 
    status = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
 
    class Meta:
        model = Lens
        fields = [
            'lensemodule',
            'assetno',  
            'location', 
            'typeitem', 
            'focallength', 
            'mountingtype', 
            'itemdesc',  
            'itempic',
            'attachment',  
            'status', 
            'createby',
        ]