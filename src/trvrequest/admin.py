from django.contrib import admin

from trvrequest.models import Travelinfo, AknowlegdeTicket
from labassets.models import Camera

admin.site.register(Travelinfo)
admin.site.register(AknowlegdeTicket)
admin.site.register(Camera)
# Register your models here.
