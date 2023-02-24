from django import forms
from labassets.models import Camera,Lens, LightingCon, Lighting,Laser,Powersupply,Cable,Card,Caltarget, Optic, Misc
from intra.settings import DATE_INPUT_FORMAT



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

    types = (
        ('', 'Please choose'),
        ('Area scan', 'Area scan'),
        ('Line scan', 'Line scan'),
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
    typeitem = forms.ChoiceField(choices=types, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
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

    types = (
        ('', 'Please choose'),
        ('Zoom Lens', 'Zoom Lens'),
        ('Telecentric Lens', 'Telecentric Lens'),
        ('CCTV Lens', 'CCTV Lens'),
        ('Objective Lens', 'Objective Lens'),
        ('N/A', 'N/A')
    )




    lensemodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lens Name / Module'}))
    assetno  =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset Number'}))
    location =  forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item location'}))
    typeitem  = forms.ChoiceField(choices=types, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
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


class LightconForm(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    lightconmodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lighting Controller Module Name'}))
    assetno  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Light Controller Asset No'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}))
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    itempic  = forms.FileField(required=False) 
    attachment   = forms.FileField(required=False) 
    status  = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
   

    class Meta:
        model = LightingCon
        fields = [
            'lightconmodule', 
            'assetno',  
            'location', 
            'itemdesc', 
            'itempic',
            'attachment', 
            'status',  
            'createby', 
        ]

class LightingForm(forms.ModelForm):

    types = (
        ('', 'Please choose'),
        ('Backlight', 'Backlight'),
        ('Bar Light', 'Bar Light'),
        ('Coaxial Light', 'Coaxial Light'),
        ('Line Light', 'Line Light'),
        ('Ring Light', 'Ring Light'),
        ('Sportlight', 'Sportlight'),
        ('N/A', 'N/A')
    )

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    color = (
        ('', 'Please choose'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('White', 'White'),
        ('RGB', 'RGB'),
        ('UV', 'UV'),
        ('IR', 'IR'),
    )

    #= forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    #= forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Light Controller Asset No'}))
    #=  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    lightingmodul = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lighting Module Name'}))
    assetno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lighting Assets Number'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item location'}))
    typeitem  = forms.ChoiceField(choices=types, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    coloritem = forms.ChoiceField(choices=color, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    wattage = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Wattage'}))
    voltage = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Voltage'}))
    currentamp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Current Amp'}))
    manufacturing = forms.DateField(input_formats=DATE_INPUT_FORMAT, required=False, widget=forms.DateInput(attrs={'class':'form-control'}))
    itempic = forms.FileField(required=False) 
    attachment = forms.FileField(required=False) 
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lighting Quantity '}))
    status= forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    itemdesc  =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Light Controller Asset No'}))

    class Meta:
        model = Lighting
        fields = [
            'lightingmodul', 
            'assetno',
            'location',
            'typeitem',  
            'coloritem', 
            'wattage', 
            'voltage', 
            'currentamp', 
            'manufacturing', 
            'itempic', 
            'attachment', 
            'quantity', 
            'status', 
            'itemdesc', 
            'createby',
        ]


class LaserForm(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    lasermodule  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Laser module name'}))
    assetno  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Laser Asset No'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}))
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    itempic  = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status  = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'create by'}))


    class Meta:
        model = Laser
        fields = [
            'lasermodule', 
            'assetno',   
            'location', 
            'itemdesc',   
            'itempic', 
            'attachment',  
            'status', 
            'createby', 
      
        ]

class PowersupplyForm(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    powermodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Power Supply Module name'}))  
    assetno  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset No'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'})) 
    voltage  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Voltage'})) 
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    itempic = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Laser module name'}))
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please state the quantity'}))

    class Meta:
        model = Powersupply
        fields = [
            'powermodule',   
            'assetno',  
            'location',  
            'voltage',   
            'itemdesc', 
            'itempic', 
            'attachment', 
            'status', 
            'createby', 
            'quantity',
        ]

class CableForm(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    cablemodule  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cable Module Name'}))
    assetsno   = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset No'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'location'}))
    itemdesc  =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    quantity  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'The Quantity'}))
    itempic = forms.FileField(required=False)
    attachment  = forms.FileField(required=False) 
    status = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Create by'}))


    class Meta:
        model = Cable
        fields = [
            'cablemodule',  
            'assetsno',   
            'location', 
            'itemdesc',  
            'quantity',  
            'itempic', 
            'attachment',   
            'status',
            'createby', 
            'quantity', 
        ]

class CardForm(forms.ModelForm):

    types = (
        ('', 'Please choose'),
        ('Controller Card', 'Controller Card'),
        ('Firewire Card', 'Firewire Card'),
        ('Frame Grabber', 'Frame Grabber'),
        ('IO Card', 'IO Card'),
        ('Network Card', 'Network Card'),
        ('Network Controller', 'Network Controller'),
        ('PCI Card', 'PCI Card'),
        ('Graphic Card', 'Graphic Card'),
        ('N/A', 'N/A')
    )

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    cardmodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Module Name'}))
    assetno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Assets Number'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}))
    itemtype  = forms.ChoiceField(choices=types, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    itempic = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status  = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cable Module Name'}))
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity Available'}))

    class Meta:
        model = Card
        fields = [
            'cardmodule', 
            'assetno', 
            'location', 
            'itemtype',  
            'itempic', 
            'attachment',
            'status', 
            'itemdesc', 
            'createby', 
            'quantity', 
        ]

class CaltargetForm(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    calmodule  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cal.Target Module Name'}))
    assetno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cal.Target Asset Number'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}))
    itempic = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cable Module Name'}))
    quantity  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cal.Target Quantity'}))

    class Meta:
        model = Caltarget
        fields = [
            'calmodule',  
            'assetno', 
            'location', 
            'itempic', 
            'attachment', 
            'status', 
            'itemdesc', 
            'createby', 
            'quantity',
        ]

class OpticForm(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    types = (
        ('', 'Please choose'),
        ('AR Glass', 'AR Glass'),
        ('Back Coat Mirror', 'Back Coat Mirror'),
        ('Beam Splitter', 'Beam Splitter'),
        ('Clear Window', 'Clear Window'),
        ('Diffuser', 'Diffuser'),
        ('Filter', 'Filter'),
        ('Front Coat Mirror', 'Front Coat Mirror'),
        ('Lens Filter', 'Lens Filter'),
        ('Polarizer', 'Polarizer'),
        ('Prism', 'Prism'),
        ('RV Mirror', 'RV Mirror'),
        ('N/A', 'N/A')
    )

    opticmodule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Optic Module Name'})) 
    assetno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Optic assets number'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}))
    itemtype = forms.ChoiceField(choices=types, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    itemdesc =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    itempic = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cable Module Name'}))
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity of items'}))

    class Meta:

        model = Optic
        fields = [
            'opticmodule',  
            'assetno', 
            'location', 
            'itemtype', 
            'itemdesc', 
            'itempic', 
            'attachment', 
            'status', 
            'createby', 
            'quantity', 
        ]

class Miscform(forms.ModelForm):

    status = (
        ('', 'Please choose'),
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )

    miscmodule  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Misc Module Name'}))
    assetno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Misc Asset Number'}))
    itemdesc  =  forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Please state the item of description', 'rows':'4'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cable Module Name'}))
    itempic  = forms.FileField(required=False)
    attachment = forms.FileField(required=False)
    status = forms.ChoiceField(choices=status, required=False, widget=forms.Select(attrs={'class':'form-select form-select-solid','data-control':'select2','data-hide-search':'true'}))
    createby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cable Module Name'}))
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity of items'}))

    class Meta:
        model = Misc
        fields = [
            'miscmodule',  
            'assetno', 
            'itemdesc',  
            'location', 
            'itempic',  
            'attachment', 
            'status', 
            'createby', 
            'quantity', 
        ]