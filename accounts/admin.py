from django.contrib import admin
from .models import CustomUser
from .models import Connection

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('id', 'username')
    list_display_links=('id', 'username')
admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.


admin.site.register(Connection)