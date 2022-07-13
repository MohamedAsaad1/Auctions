from django.contrib import admin
from .models import *
# Register your models 
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id","title")

admin.site.register(Listings,ListingsAdmin)
admin.site.register(Categories)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(User)