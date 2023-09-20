from django.contrib import admin
from staff.models import Categories,StaffDetails,Brand,Medicine

# Register your models here.

admin.site.register(Brand)

admin.site.register(StaffDetails)

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['medicine', 'description']

admin.site.register(Medicine,ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"link":['category',]}

admin.site.register(Categories,CategoryAdmin)
