
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
    path('labsystem/camera/all_camera',labviews.table_camera, name="table_camera"),

    path('labsystem/lens/add_lens',labviews.add_lens, name='add_lens'),
    path('labsystem/lens/edit_lens/<int:pk>',labviews.edit_lens, name="edit_lens"),
    path('labsystem/lens/all_lens',labviews.table_lens, name="table_lens"),

    path('labsystem/lightcontroller/add_lightingcontroller',labviews.add_lightingcontroller, name='add_lightingcontroller'),
    path('labsystem/lightcontroller/edit_lightingcontroller/<int:pk>',labviews.edit_lightingcontroller, name="edit_lightingcontroller"),
    path('labsystem/lightcontroller/all_lighting_controller',labviews.table_lightingcontroller, name="table_lightingcontroller"),

    path('labsystem/lighting/add_lighting',labviews.add_lighting, name='add_lighting'),
    path('labsystem/lighting/edit_lighting/<int:pk>',labviews.edit_lighting, name="edit_lighting"),
    path('labsystem/lighting/all_lighting',labviews.table_lighting, name="table_ligthing"),

    path('labsystem/laser/add_laser',labviews.add_laser, name='add_laser'),
    path('labsystem/laser/edit_laser/<int:pk>',labviews.edit_laser, name="edit_laser"),
    path('labsystem/laser/all_laser',labviews.table_laser, name="table_laser"),

    path('labsystem/powersupply/add_power',labviews.add_power, name='add_power'),
    path('labsystem/powersupply/edit_power/<int:pk>',labviews.edit_power, name="edit_power"),
    path('labsystem/powersupply/all_power',labviews.table_power, name="table_power"),

    path('labsystem/cable/add_cable',labviews.add_cable, name='add_cable'),
    path('labsystem/cable/edit_cable/<int:pk>',labviews.edit_cable, name="edit_cable"),
    path('labsystem/cable/all_cable',labviews.table_cable, name="table_cable"),

    path('labsystem/card/add_card',labviews.add_card, name='add_card'),
    path('labsystem/card/edit_card/<int:pk>',labviews.edit_card, name="edit_card"),
    path('labsystem/card/all_card',labviews.table_card, name="table_card"),

    path('labsystem/caltarget/add_cal',labviews.add_cal, name='add_cal'),
    path('labsystem/caltarget/edit_cal/<int:pk>',labviews.edit_cal, name="edit_cal"),
    path('labsystem/caltarget/all_cal',labviews.table_cal, name="table_cal"),

    path('labsystem/optic/add_optic',labviews.add_optic, name='add_optic'),
    path('labsystem/optic/edit_optic/<int:pk>',labviews.edit_optic, name="edit_optic"),
    path('labsystem/optic/all_optic',labviews.table_optic, name="table_optic"),

    path('labsystem/misc/add_misc',labviews.add_misc, name='add_misc'),
    path('labsystem/misc/edit_misc/<int:pk>',labviews.edit_misc, name="edit_misc"),
    path('labsystem/misc/all_misc',labviews.table_misc, name="table_misc"),

    path('labsystem/items/details/<str:arg>/<int:pk>',labviews.lab_details, name="lab_details"),

    path('admin/', admin.site.urls),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),   # our pre-configured msal URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
