from django.contrib import admin

# Register your models here.


from homebase.models import Specialuser, Userprofile

# Register your models here.
admin.site.register(Specialuser)
admin.site.register(Userprofile)
