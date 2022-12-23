from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
import requests

ms_identity_web = settings.MS_IDENTITY_WEB

# Create your views here.
def labdash(request):

    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    context = {
        'profile':dict(results),
    }
   
    return render(request, 'pages/labsystem/index.html',context)