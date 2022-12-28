from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from labassets.models import Camera, Lens
from labassets.forms import CameraForm, LensForms
import requests

ms_identity_web = settings.MS_IDENTITY_WEB

# Create your views here.
def labdash(request):

    context = {
        
    }
   
    return render(request, 'pages/labsystem/index.html',context)

#camera section
def add_camera(request):

    form = CameraForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form =  CameraForm()
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


#lense section
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