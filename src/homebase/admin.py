from django.contrib import admin

# Register your models here.


from homebase.models import Specialuser, Userprofile, ApplicationPerm,Systemsetting

# Register your models here.
admin.site.register(Specialuser)
admin.site.register(Userprofile)
admin.site.register(ApplicationPerm)
admin.site.register(Systemsetting)
