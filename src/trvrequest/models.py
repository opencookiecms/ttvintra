from django.db.models.deletion import CASCADE
from django.db import models

# Create your models here.
class Travelinfo(models.Model):
    offid = models.CharField(max_length=200, null=True, blank=True)
    companyname = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    emailname = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    travelpurpose = models.CharField(max_length=200, null=True, blank=True)
    customername = models.CharField(max_length=100, null=True, blank=True)
    projectcode = models.CharField(max_length=20, null=True, blank=True)
    destinations = models.CharField(max_length=150, null=True, blank=True)
    datearrive = models.DateField(null=True, blank=True)
    datereturn = models.DateField(null=True, blank=True)
    timearrive = models.CharField(max_length=20, blank=True, null=True)
    timereturn = models.CharField(max_length=20, blank=True, null=True)
    transport = models.CharField(max_length=20, null=True, blank=True)
    airlinepreferred = models.CharField(max_length=10, null=True, blank=True)
    seatingpreferred = models.CharField(max_length=10, null=True, blank=True)
    luggageneeded = models.CharField(max_length=10, null=True, blank=True)
    luggageweight = models.CharField(max_length=10, null=True, blank=True)
    luggagereason = models.CharField(max_length=200, null=True, blank=True)
    hotelneeded = models.CharField(max_length=10, null=True, blank=True)
    numbernights = models.CharField(max_length=10, null=True, blank=True)
    hotellocation = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    hodstatus = models.CharField(max_length=10, null=True, blank=True)
    drstatus = models.CharField(max_length=10, null=True, blank=True)
    hodapproval = models.CharField(max_length=150, null=True, blank=True)
    hodemail = models.CharField(max_length=150, blank=True, null=True)
    directorapproval = models.CharField(max_length=150, null=True, blank=True)
    dremail = models.CharField(max_length=150, blank=True, null=True)
    createby = models.CharField(max_length=150, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True, editable=False)
    updatedat = models.DateTimeField(auto_now=True, editable=False)

class AknowlegdeTicket(models.Model):
    transport = models.CharField(max_length=50, null=True, blank=True)
    issuetref = models.CharField(max_length=150, null=True, blank=True)
  
    issuetdate = models.DateField(null=True, blank=True)
  
    issuelink = models.CharField(max_length=250, null=True, blank=True)
    issuefile = models.FileField(null=True, blank=True)


    createby = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    issuerelate = models.ForeignKey(Travelinfo, blank=True, null=True, on_delete=CASCADE)

