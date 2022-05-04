from django.contrib import admin
from .models import Category,GumiPost,Powder,Maker,Hard
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class GumiPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class MakerAdmin(admin.ModelAdmin):
    list_display=('id','makername')
    list_display_links=('id','makername')

class PowderAdmin(admin.ModelAdmin):
    list_display=('id','powderis')
    list_display_links=('id','powderis')

class HardAdmin(admin.ModelAdmin):
    list_display=('id','hardness')
    list_display_links=('id','hardness')
                        
admin.site.register(Category,CategoryAdmin)
admin.site.register(GumiPost,GumiPostAdmin)
admin.site.register(Maker,MakerAdmin)
admin.site.register(Powder,PowderAdmin)
admin.site.register(Hard,HardAdmin)
# Register your models here.
