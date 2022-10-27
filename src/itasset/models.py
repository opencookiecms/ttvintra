from django.db import models

# Create your models here.

class Assetlist(models.Model):
    assetnum = models.CharField(max_length=50, null=True, blank=True) 
    assettagno = models.CharField(max_length=50, null=True, blank=True) 
    assetinvdate = models.DateField(null=True, blank=True)
    assetinvno = models.CharField(max_length=50, null=True, blank=True) 
    assetponumber = models.CharField(max_length=50, null=True, blank=True) 
    assetcost = models.CharField(max_length=20, null=True, blank=True) 
    assetcc = models.CharField(max_length=10, null=True, blank=True)
    assetstatus = models.CharField(max_length=20, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

class ComputerList(models.Model):
    compmodel = models.CharField(max_length=100, null=True, blank=True) 
    compbrand = models.CharField(max_length = 50, null=True, blank=True) 
    compserialnumber = models.CharField(max_length=50, null=True, blank=True) 
    compprocessor = models.CharField(max_length=20, null=True, blank=True) 
    compgraphic = models.CharField(max_length=50, null=True, blank=True) 
    compram = models.CharField(max_length=20, null=True, blank=True) 
    compstorage  = models.CharField(max_length=20, null=True, blank=True) 
    compos = models.CharField(max_length=20, null=True, blank=True) 
    compdisplay = models.CharField(max_length=20, null=True, blank=True) 
    department = models.CharField(max_length=50, null=True, blank=True) 
    owner1 = models.CharField(max_length=150, null=True, blank=True) 
    owner2 = models.CharField(max_length=150, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

