from django.conf import settings
from django.shortcuts import render, redirect
from django.conf import settings
from trvrequest.forms import TicketForm, TravelRequestForm
from django.core import serializers


import requests

from trvrequest.models import Travelinfo

ms_identity_web = settings.MS_IDENTITY_WEB

# Create your views here.
@ms_identity_web.login_required
def traveladd(request):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization': authz}).json()

    form = TravelRequestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = TravelRequestForm
            return redirect('tvrdashboard')
        else:
            print(form.errors)
            print('fail to save the data')
    context = {
        'profile':dict(results),
        'titlehead':'Travel Request - Add New',
        'traveladd':True,
        'form':form
    }
    return render(request, 'pages/travelrequest/traveladd.html',context)

@ms_identity_web.login_required
def dashboard(request):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()
   

    msid = results['id']
    travelobj = Travelinfo.objects.filter(offid=msid)
    total = Travelinfo.objects.filter(offid=msid).count()
    new = Travelinfo.objects.filter(offid=msid,status="New").count()
    pending = Travelinfo.objects.filter(offid=msid,status="Pending").count()
    decline = Travelinfo.objects.filter(offid=msid,status="Decline").count()
 

    context = {
    
        'obj':travelobj,
        'profile':dict(results),
        'traveldashboard':True,
        'titlehead':'TT Vision - My Travel Request',
        'total':total,
        'new':new,
        'pending':pending,
        'decline':decline,

    }
    return render(request, 'pages/travelrequest/dashboard.html',context)

@ms_identity_web.login_required
def traveloverview(request, id):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    travel = Travelinfo.objects.get(id=id)

    context = {
        'profile':dict(results),
        'overview':True,
        'titlehead':'Travel Request Details',
        'travel':travel
    }
    return render(request, 'pages/travelrequest/overview.html',context)

def ticketissue(request, id):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    travel = Travelinfo.objects.get(id=id)

    form = TicketForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = TicketForm()
        else:
            print('failed')


    context = {
        'akticket':True,
        'profile':dict(results),
        'overview':True,
        'titlehead':'Travel Request Details',
        'travel':travel,
        'form':form,
    }
    
    return render(request, 'pages/ticket/ticketissue.html',context)



