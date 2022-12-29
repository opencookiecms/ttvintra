
from django.contrib import admin
from django.urls import path, include, re_path

from homebase import views
from trvrequest import views as trviews
from labassets import views as labviews
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
    path('travelrequest/list',trviews.travelist, name="travellist"),
    path('travelrequest/overview/<int:id>',trviews.traveloverview, name='overview'),
    path('travelrequest/approval/<int:id>', trviews.approval, name="approval"),
    path('travelrequest/edit/<int:id>', trviews.travelmodified, name="traveledit"),

    path('labsystem/dashboard', labviews.labdash, name="labindex"),

    path('labsystem/camera/add_camera',labviews.add_camera, name='add_camera'),
    path('labsystem/camera/edit_camera/<int:pk>',labviews.edit_camera, name="edit_camera"),

    path('labsystem/lens/add_lens',labviews.add_lens, name='add_lens'),
    path('labsystem/lens/edit_lens/<int:pk>',labviews.edit_lens, name="edit_lens"),

    path('labsystem/lightcontroller/add_lightingcontroller',labviews.add_lightingcontroller, name='add_lightingcontroller'),
    path('labsystem/lightcontroller/edit_lightingcontroller/<int:pk>',labviews.edit_lightingcontroller, name="edit_lightingcontroller"),

    path('labsystem/lighting/add_lighting',labviews.add_lens, name='add_lighting'),
    path('labsystem/lighting/edit_lighting/<int:pk>',labviews.edit_lens, name="edit_lighting"),

    path('admin/', admin.site.urls),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),   # our pre-configured msal URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
