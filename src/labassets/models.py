from django.db import models

# Create your models here.

class Camera(models.Model):
    cameramodule = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True) 
    location  = models.CharField(max_length=50, null=True, blank=True) 
    typeitem = models.CharField(max_length=50, null=True, blank=True) 
    resolution = models.CharField(max_length=50, null=True, blank=True) 
    isomark = models.CharField(max_length=50, null=True, blank=True) 
    mountingtype = models.CharField(max_length=50, null=True, blank=True) 
    interfacetype = models.CharField(max_length=50, null=True, blank=True) 
    
    itempic = models.CharField(max_length=50, null=True, blank=True) 
    attachment = models.CharField(max_length=50, null=True, blank=True) 
    status  = models.CharField(max_length=50, null=True, blank=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Lens(models.Model):
    lensemodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    typeitem
    focallenth
    mountingtype
    itemdesc = models.TextField(null=True, blank=True) 
    itempic = models.CharField(max_length=50, null=True, blank=True) 
    attachment = models.CharField(max_length=50, null=True, blank=True)
    status  = models.CharField(max_length=50, null=True, blank=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class LightingCon(models.Model):

    lightconmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno  = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True) 
    itempic = models.CharField(max_length=50, null=True, blank=True) 
    attachment = models.CharField(max_length=50, null=True, blank=True)
    status  = models.CharField(max_length=50, null=True, blank=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Lighting(models.Model):

    lightingmodul  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    typeitem
    coloritem
    wattage
    voltage
    currentamp
    manufacturing
    itempic
    attachment
    quantity
    status
    itemdesc = models.TextField(null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Laser(models.Model):
    lasermodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno  = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True)  
    attachment
    itempic
    status
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Powersupply(models.Model):
    powermodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno  = models.CharField(max_length=50, null=True, blank=True) 
    location  = models.CharField(max_length=50, null=True, blank=True)
    voltage 
    itemdesc = models.TextField(null=True, blank=True)  
    attachement
    itempic
    status
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Cable(models.Model):
    cablemodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetsno = models.CharField(max_length=50, null=True, blank=True)  
    location = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True) 
    quantity 
    quantityaval
    attachment
    itempic 
    status
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Card(models.Model):
    cardmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)  
    location  = models.CharField(max_length=50, null=True, blank=True)
    itemtype 
    attachment
    itempic 
    status
    itemdesc = models.TextField(null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Caltarget(models.Model):
    calmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)  
    location = models.CharField(max_length=50, null=True, blank=True)
    itempic
    attachment 
    status
    itemdesc = models.TextField(null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Optic(models.Model):
    opticmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)  
    location  = models.CharField(max_length=50, null=True, blank=True)
    itemtype
    attachment
    itemdesc = models.TextField(null=True, blank=True) 
    itempic
    status
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class Misc(models.Model):
    miscmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True)  
    location = models.CharField(max_length=50, null=True, blank=True)
    itempic
    attachment 
    status
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

    









