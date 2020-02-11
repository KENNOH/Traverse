from django.contrib import admin
from .models import Location, Hotel, Accomodation, Category

# Register your models here.

class EventModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = []
    list_per_page = 20
    list_editable = []

    class Meta:
        model = Location
admin.site.register(Location, EventModelAdmin)


class EventModelAdmin1(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = []
    list_per_page = 20
    list_editable = []

    class Meta:
        model = Category


admin.site.register(Category, EventModelAdmin1)
