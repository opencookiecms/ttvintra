from django.urls import reverse
from django.conf import settings

import requests
ms_identity_web = settings.MS_IDENTITY_WEB

def context(request):
    claims = request.identity_context_data._id_token_claims
    exclude_claims = ['iat', 'exp', 'nbf', 'uti', 'aio', 'rh']
    claims_to_display = {claim: value for claim, value in claims.items() if claim not in exclude_claims}

    client_id=settings.AAD_CONFIG.client.client_id
    aad_link="https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/Authentication/appId/" + client_id +"/isMSAApp/"
    
    return dict(claims_to_display=claims_to_display,
                redirect_uri_external_link = request.build_absolute_uri(reverse(settings.AAD_CONFIG.django.auth_endpoints.redirect)),
                aad_link=aad_link)


def profile(request):
    
    ms_identity_web.acquire_token_silently()
    graphz = 'https://graph.microsoft.com/beta/me'
    authz = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graphz, headers={'Authorization':authz}).json()

    return {"profile":dict(results)}
