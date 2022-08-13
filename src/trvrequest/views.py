from django.conf import settings
from django.shortcuts import render, redirect
from django.conf import settings
from homebase.models import ApplicationPerm
from trvrequest.forms import TicketForm, TravelRequestForm, TraveleditForm
from django.core import serializers
from django.db.models import Q

import requests

from trvrequest.models import AknowlegdeTicket, Travelinfo

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
    email = results['mail']
    admintravel = ApplicationPerm.objects.filter(userlink__mailaddress=email).first()
    traveall = Travelinfo.objects.all().count()
    travelobj = Travelinfo.objects.filter(offid=msid)
    travelsub = Travelinfo.objects.filter(Q(hodemail=email) | Q(dremail=email))
    total = Travelinfo.objects.filter(offid=msid).count()
    new = Travelinfo.objects.filter(offid=msid,status="New").count()
    pending = Travelinfo.objects.filter(offid=msid,status="Pending").count()
    decline = Travelinfo.objects.filter(offid=msid,status="Decline").count()
    subo = Travelinfo.objects.filter(Q(hodemail=email) | Q(dremail=email)).count()

    print(admintravel)

    context = {
    
        'obj':travelobj,
        'obj2':travelsub,
        'profile':dict(results),
        'traveldashboard':True,
        'titlehead':'TT Vision - My Travel Request',
        'total':total,
        'subo':subo,
        'new':new,
        'pending':pending,
        'decline':decline,
        'appperm':admintravel,
        'totalall':traveall,

    }
    return render(request, 'pages/travelrequest/dashboard.html',context)

@ms_identity_web.login_required
def traveloverview(request, id):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    travel = Travelinfo.objects.get(id=id)
    ticked = AknowlegdeTicket.objects.filter(id=id).first()


    context = {
        'profile':dict(results),
        'overview':True,
        'titlehead':'Travel Request Details',
        'travel':travel,
        'ticked':ticked
    }
    return render(request, 'pages/travelrequest/overview.html',context)

@ms_identity_web.login_required
def ticketissue(request, id):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    travel = Travelinfo.objects.get(id=id)
    ticket = AknowlegdeTicket.objects.filter(id=id).first()

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
        'ticked':ticket,
    }
    
    return render(request, 'pages/ticket/ticketissue.html',context)

@ms_identity_web.login_required
def travelmodified(request, id):

    
    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    travel = Travelinfo.objects.get(id=id)

    dataobject = travel

    form = TraveleditForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = TraveleditForm()
        return redirect('tvrdashboard')
    else:
        print('failed')

    context = {
        'editravel':True,
        'travel':travel,
        'profile':dict(results),
        'titlehead':'Travel Request Edit',
        'form':form
    }

    return render(request, 'pages/travelrequest/modified.html',context)


@ms_identity_web.login_required
def approval(request, id):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    travel = Travelinfo.objects.get(id=id)
    ticked = AknowlegdeTicket.objects.filter(id=id).first()


    context = {
        'profile':dict(results),
        'overview':True,
        'titlehead':'Travel Request Details',
        'travel':travel,
        'ticked':ticked
    }
    return render(request, 'pages/travelrequest/overviewapproval.html',context)



