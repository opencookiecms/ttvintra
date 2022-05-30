from django.conf import settings
from django.shortcuts import render, redirect
from django.conf import settings
import json
from trvrequest.forms import TravelRequestForm


import requests

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
            return redirect('')
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