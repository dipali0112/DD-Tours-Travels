from django.contrib import admin
from .models import Location, Contact, Itinerary, Inquiry

class ItineraryInline(admin.TabularInline):  # Inline form for Itinerary in LocationAdmin
    model = Itinerary
    extra = 1  # Shows 1 empty form by default
    fields = ('day', 'DDate', 'description')
    ordering = ['day']
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'difficulty', 'price')
    search_fields = ('name', 'difficulty')
    inlines = [ItineraryInline]
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('location', 'day', 'DDate', 'description')
    search_fields = ('location__name', 'day')
    list_filter = ('location',)
