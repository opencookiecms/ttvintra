import imp
from django.conf import settings
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from homebase.models import Userprofile, Specialuser
from homebase.forms import userprofileForm


ms_identity_web = settings.MS_IDENTITY_WEB
# Create your views here.
@ms_identity_web.login_required
def index(request):
    
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/beta/me'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()

    oid = results['id']
    offid = Userprofile.objects.filter(offid=oid).first()

    
    context = {
        'theid':offid,
        'profile':dict(results),
        'title':'Application',
        'titlehead':'My Dashboard'
    }
    return render(request, 'pages/dashboard/hub.html',context)


@ms_identity_web.login_required
def prereg(request):

    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/beta/me'
    graph2 = 'https://graph.microsoft.com/v1.0/users'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()
    results2 =  requests.get(graph2, headers={'Authorization':authZ}).json()

   
    tokenclaim = request.identity_context_data._id_token_claims

    sub = tokenclaim['sub']

    if 'value' in results2:
        results2 ['num_results'] = len(results2['value'])
        results2['value'] = results2['value'][:120]
    else:
        results2['value'] =[{'displayName': 'call-graph-error','mail':'call-graph-error'}]

    

    form = userprofileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = userprofileForm()
        return redirect('index')
    else:
        print(form.errors)

    context = {
        'form':form,
        'titlehead':'Pre Register',
        'prereg':True,
        'profile':dict(results),
        'results2':dict(results2),
        'sub':sub,
       
    }
    return render(request, 'pages/prereg/prereg.html',context)



def loademailhod(request):
    userid = request.GET.get('id')
    print(userid)
    getmail = Specialuser.objects.filter(id=userid)

    return render(request, 'pages/loadmailhod.html',{'getmail':getmail})

def loademaildirector(request):
    userid = request.GET.get('id')
    print(userid)
    getmail = Specialuser.objects.filter(id=userid)

    return render(request, 'pages/loadmaildirector.html',{'getmail':getmail})

