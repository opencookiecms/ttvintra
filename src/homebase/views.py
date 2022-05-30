from django.conf import settings
from django.shortcuts import render, redirect
from django.conf import settings
import requests




ms_identity_web = settings.MS_IDENTITY_WEB
# Create your views here.
@ms_identity_web.login_required
def index(request):
    
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/beta/me'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()

    
    context = {
        'title':'Application',
        'titlehead':'My Dashboard'
    }
    return render(request, 'pages/hub.html',context)

