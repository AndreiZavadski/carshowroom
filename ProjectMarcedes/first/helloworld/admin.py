from django.contrib import admin
from .models import Mercedes, Provider_of_cars

# Register your models here.

@admin.register(Mercedes)
class mercedesAdmin(admin.ModelAdmin):
    list_display = ['brand', 'provider', 'price']
    search_fields = ['brand__istartswith']
    list_per_page = 3

@admin.register(Provider_of_cars)
class Provider_of_carsAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email']