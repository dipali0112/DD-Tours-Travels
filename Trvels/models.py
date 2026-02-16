from django.db import models
import random
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.conf import settings

class OTPVerification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()
        return self.otp


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    number_of_persons = models.IntegerField()
    departure_date = models.DateField()
    return_date = models.DateField()
# <<<<<<< HEAD
    transportation_method = models.CharField(
        max_length=10, 
        choices=[('Flight', 'Flight'), ('Train', 'Train')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

# =======
#     transportation_method = models.CharField(max_length=10, choices=[('Flight', 'Flight'), ('Train', 'Train')])
    
# >>>>>>> dd_tours_travels/main
    def __str__(self):
        return f"Inquiry from {self.name} for {self.place}"

class Location(models.Model):
# <<<<<<< HEAD
#     line = models.TextField(null=True, blank=True)
#     Cname = models.CharField(max_length=255, default="India")
# =======
    line = models.TextField(null=True)
    Cname = models.CharField(max_length=255,default="India") 
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    age_group = models.CharField(max_length=255)
    altitude = models.CharField(max_length=255)
# <<<<<<< HEAD
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     includes = models.JSONField(default=list)
#     about = models.TextField()
#     image = models.ImageField(upload_to='location_images/')
#     brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
#     backimage = models.ImageField(upload_to='location_images/', null=True, blank=True)

#     def __str__(self):
#         return self.name

# class Itinerary(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="itinerary")
#     DDate = models.DateField()
#     day = models.IntegerField()
#     description = models.TextField()

#     class Meta:
#         ordering = ['day']  # Ensures correct order in admin & frontend

#     def __str__(self):
#         return f"Day {self.day} - {self.location.name}"
# =======
    price = models.CharField(max_length=255)
    includes = models.JSONField()  # To store a list of inclusions
    about = models.TextField()
    image = models.CharField(max_length=255) 
    brochure = models.FileField(upload_to='brochures/', null=True, blank=True)
    backimage = models.CharField(null=True,max_length=255) 
    
    def __str__(self):
        return self.name
    
class TravelLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="trsvels_locations")
    place_name = models.CharField(max_length=100)  # e.g., Kochi, Munnar
    latitude = models.FloatField()
    longitude = models.FloatField()
    sequence = models.IntegerField()  # Order of visit

    class Meta:
        ordering = ["location", "sequence"]  # Ensures correct order

    def __str__(self):
        return f"{self.location.name} - {self.place_name}"
    
    
class Itinerary(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="itineraries")
    days_count = models.IntegerField()

    def __str__(self):
        return f"{self.location.name} - {self.days_count} Days"


# Day-wise Itinerary Table
class ItineraryDay(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name="days")
    day_number = models.IntegerField()
    short_description = models.CharField(max_length=255)
    detailed_description = models.TextField()

    def __str__(self):
        return f"Day {self.day_number}: {self.short_description} - {self.itinerary.location.name}"


# Detailed Day-wise Activities Table
class DayActivity(models.Model):
    itinerary_day = models.ForeignKey(ItineraryDay, on_delete=models.CASCADE, related_name="activities")
    time = models.TimeField()
    activity_description = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.time} - {self.activity_description} ({self.place})"


class CustomUser(AbstractUser):
    # Add any custom fields if needed
    custom_field = models.CharField(max_length=100, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Change the related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Change the related_name
        blank=True
    )

    def __str__(self):
        return self.username
