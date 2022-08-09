from django.db import models

# Create your models here.

class Userprofile(models.Model):
    employeeid = models.CharField(max_length=20, null=True, blank=True) 
    givename = models.CharField(max_length=150, null=True, blank=True)
    displayname = models.CharField(max_length=150, null=True, blank=True)
    mailaddress = models.CharField(max_length=150, null=True, blank=True)
    offid = models.CharField(max_length=250, null=True, blank=True)
    subid = models.CharField(max_length=250, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department  = models.CharField(max_length=50, blank=True, null=True)
    userstatus  = models.CharField(max_length=50, blank=True, null=True)
    supervisor1 = models.CharField(max_length=100, null=True, blank=True)
    supervisor2 = models.CharField(max_length=100, null=True, blank=True)
    supervisor3 = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.displayname


class Specialuser(models.Model):
    specialname = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    linkup = models.ForeignKey(Userprofile, blank=True, null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.specialname

class ApplicationPerm(models.Model):
    
    travelrequest = models.BooleanField()
    shipmentrequest = models.BooleanField()
    ncar  = models.BooleanField()
    userlink = models.ForeignKey(Userprofile, blank=True, null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.userlink.displayname
