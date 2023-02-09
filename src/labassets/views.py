from django.shortcuts import render,redirect
from django.conf import settings
from django.db.models import Q
from labassets.models import Camera, Lens,LightingCon, Lighting, Laser, Powersupply, Cable, Card, Caltarget, Optic,Misc
from labassets.forms import CameraForm, LensForms,LightconForm, LightingForm, LaserForm, PowersupplyForm,CableForm,CardForm,CaltargetForm,OpticForm, Miscform
import requests

ms_identity_web = settings.MS_IDENTITY_WEB

# Create your views here.
def labdash(request):

    cam = Camera.objects.all().count()
    len = Lens.objects.all().count()
    lthcon = LightingCon.objects.all().count()
    lgtg = Lighting.objects.all().count()
    laser = Laser.objects.all().count()
    pwr = Powersupply.objects.all().count()
    cab = Cable.objects.all().count()
    card = Card.objects.all().count()
    cal = Caltarget.objects.all().count()
    opc = Optic.objects.all().count()
    misc = Misc.objects.all().count()

    context = {
        'cam':cam,
        'len':len,
        'lthcon':lthcon,
        'lgtg':lgtg,
        'laser':laser,
        'pwr':pwr,
        'cab':cab,
        'card':card,
        'cal':cal,
        'opc':opc,
        'misc':misc,
    }
   
    return render(request, 'pages/labsystem/index.html',context)

#camera section
def add_camera(request):

    form = CameraForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  CameraForm()
        return redirect('table_camera')
    else:
        print('unable to complie unit error')
        print(form.errors)
     

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/camera_add_update.html',context)

def edit_camera(request, pk):

    objectdata = Camera.objects.get(pk=pk)
    form = CameraForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/camera_add_update.html',context)

def table_camera(request):
    table = Camera.objects.all()
    tc = Camera.objects.all().count()

    context = {
        'tab':table,
        'tc':tc,
        'cv':True,
    }

    return render(request,'pages/labsystem/camera_allv.html',context)


#lens section
def add_lens(request):

    form = LensForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  LensForms()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/lens_add_update.html',context)

def edit_lens(request, pk):

    objectdata = Lens.objects.get(pk=pk)
    form = LensForms(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/lens_add_update.html',context)


#lighting controller section
def add_lightingcontroller(request):

    form = LightconForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  LightconForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/lightingcontroller_add_update.html',context)

def edit_lightingcontroller(request, pk):

    objectdata = LightingCon.objects.get(pk=pk)
    form = LightconForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/lightingcontroller_add_update.html',context)

#lighting section
def add_lighting(request):

    form = LightingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  LightingForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/lighting_add_update.html',context)

def edit_lighting(request, pk):

    objectdata = Lighting.objects.get(pk=pk)
    form = LightingForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/lighting_add_update.html',context)


#laser section
def add_laser(request):

    form = LaserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  LaserForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/laser_add_update.html',context)

def edit_laser(request, pk):

    objectdata = Laser.objects.get(pk=pk)
    form = LaserForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/laser_add_update.html',context)


#power supply section
def add_power(request):

    form = PowersupplyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  PowersupplyForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/power_add_update.html',context)

def edit_power(request, pk):

    objectdata = Powersupply.objects.get(pk=pk)
    form = PowersupplyForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/power_add_update.html',context)


#cable section
def add_cable(request):

    form = CableForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  CableForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/cable_add_update.html',context)

def edit_cable(request, pk):

    objectdata = Cable.objects.get(pk=pk)
    form = CableForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/cable_add_update.html',context)

#card section
def add_card(request):

    form = CardForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  CardForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/card_add_update.html',context)

def edit_card(request, pk):

    objectdata = Card.objects.get(pk=pk)
    form = CardForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/card_add_update.html',context)


#CAL. Target section
def add_cal(request):

    form = CaltargetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  CaltargetForm()
    else:
        print('unable to complie unit error')
        print(form.errors)

    context = {
        'form':form,
        'create':True,
    }
   
    return render(request, 'pages/labsystem/forms/cal_add_update.html',context)

def edit_cal(request, pk):

    objectdata = Caltarget.objects.get(pk=pk)
    form = CaltargetForm(request.POST or None, request.FILES or None, instance=objectdata)

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        print('unable to update this data')

    context = {
        'form':form,
        'update':True,
        'data':objectdata,
    }

    return render(request, 'pages/labsystem/forms/cal_add_update.html',context)