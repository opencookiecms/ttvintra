from django.db import models
from django.conf import settings
from storages.backends.sftpstorage import SFTPStorage

fs = SFTPStorage()


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
    itempic = models.ImageField(upload_to='photos/camera', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/camera', storage=fs, null=True, blank=True) 
    status  = models.CharField(max_length=50, null=True, blank=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)

class Lens(models.Model):
    lensemodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    typeitem = models.CharField(max_length=50, null=True, blank=True) 
    focallength = models.CharField(max_length=50, null=True, blank=True) 
    mountingtype = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True) 
    itempic = models.ImageField(upload_to='photos/lens', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/lens', storage=fs,null=True, blank=True) 
    status  = models.CharField(max_length=50, null=True, blank=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)

class LightingCon(models.Model):

    lightconmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno  = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True) 
    itempic = models.ImageField(upload_to='photos/lightingcontroller', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/lightingcontroller', storage=fs, null=True, blank=True) 
    status  = models.CharField(max_length=50, null=True, blank=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)

class Lighting(models.Model):

    lightingmodul  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    typeitem = models.CharField(max_length=50, null=True, blank=True) 
    coloritem = models.CharField(max_length=50, null=True, blank=True) 
    wattage = models.CharField(max_length=50, null=True, blank=True) 
    voltage = models.CharField(max_length=50, null=True, blank=True) 
    currentamp = models.CharField(max_length=50, null=True, blank=True) 
    manufacturing = models.DateField(null=True, blank=True)
    itempic = models.ImageField(upload_to='photos/lighting', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/lighting', storage=fs, null=True, blank=True) 
    quantity = models.CharField(max_length=50, null=True, blank=True) 
    status = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)

class Laser(models.Model):
    lasermodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno  = models.CharField(max_length=50, null=True, blank=True) 
    location = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True)  
    itempic = models.ImageField(upload_to='photos/laser', storage=fs,  null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/laser', storage=fs,null=True, blank=True) 
    status = models.CharField(max_length=50, null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)

class Powersupply(models.Model):
    powermodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno  = models.CharField(max_length=50, null=True, blank=True) 
    location  = models.CharField(max_length=50, null=True, blank=True)
    voltage  = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True)  
    itempic = models.ImageField(upload_to='photos/power', storage=fs,  null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/power', storage=fs, null=True, blank=True) 
    status = models.CharField(max_length=50, null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)
    quantity  = models.IntegerField(null=True, blank=True) 

class Cable(models.Model):
    cablemodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetsno = models.CharField(max_length=50, null=True, blank=True)  
    location = models.CharField(max_length=50, null=True, blank=True)
    itemdesc = models.TextField(null=True, blank=True) 
    quantity  = models.IntegerField(null=True, blank=True) 
    itempic = models.ImageField(upload_to='photos/cable', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/cable', storage=fs, null=True, blank=True)  
    status = models.CharField(max_length=50, null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)
  

class Card(models.Model):
    cardmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)  
    location  = models.CharField(max_length=50, null=True, blank=True)
    itemtype  = models.CharField(max_length=50, null=True, blank=True) 
    itempic = models.ImageField(upload_to='photos/card', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/card', storage=fs,null=True, blank=True)  
    status = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)
    quantity  = models.IntegerField(null=True, blank=True) 

class Caltarget(models.Model):
    calmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)  
    location = models.CharField(max_length=50, null=True, blank=True)
    itempic = models.ImageField(upload_to='photos/caltarget', storage=fs,null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/caltarget', storage=fs, null=True, blank=True) 
    status = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)
    quantity  = models.IntegerField(null=True, blank=True) 

class Optic(models.Model):
    opticmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True)  
    location  = models.CharField(max_length=50, null=True, blank=True)
    itemtype = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True) 
    itempic = models.ImageField(upload_to='photos/optic', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/optic', storage=fs, null=True, blank=True) 
    status = models.CharField(max_length=50, null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)
    quantity  = models.IntegerField(null=True, blank=True) 

class Misc(models.Model):
    miscmodule  = models.CharField(max_length=100, null=True, blank=True) 
    assetno = models.CharField(max_length=50, null=True, blank=True) 
    itemdesc = models.TextField(null=True, blank=True)  
    location = models.CharField(max_length=50, null=True, blank=True)
    itempic = models.ImageField(upload_to='photos/misc', storage=fs, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/misc', storage=fs,null=True, blank=True) 
    status = models.CharField(max_length=50, null=True, blank=True) 
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True, editable=False)
    updatedate = models.DateTimeField(auto_now=True, editable=False)
    quantity  = models.IntegerField(null=True, blank=True)


class Loanitem(models.Model):
    requester = models.CharField(max_length=100, null=True, blank=True) 
    requestdate = models.DateField(null=True, blank=True)
    returndate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True) 
    attachment = models.FileField(upload_to='attachment/loan', storage=fs, null=True, blank=True) 
    approval = models.CharField(max_length=100, null=True, blank=True)



    









