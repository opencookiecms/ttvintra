
from django.contrib import admin
from django.urls import path, include, re_path

from homebase import views
from trvrequest import views as trviews
from django.conf import settings
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [

    path('',views.index, name='index'),
    path('prereg', views.prereg, name='prereg'),
    path('acknowledgement/travel/<int:id>', trviews.ticketissue, name="akticket"),

    path('loadmailhod', views.loademailhod, name="hodmail"),
    path('loadmaindirector', views.loademaildirector, name="drdmail"),


    path('travelrequest/add', trviews.traveladd, name='traveladd'),
    path('travelrequest/dashboard', trviews.dashboard, name='tvrdashboard'),
    path('travelrequest/overview/<int:id>',trviews.traveloverview, name='overview'),
    path('admin/', admin.site.urls),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),   # our pre-configured msal URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
