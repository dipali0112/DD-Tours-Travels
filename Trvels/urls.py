from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact_view, name='contact'),
    path('location/<int:id>/', views.location, name='location'), 
    path('inquiry/', views.inquiry_form, name='inquiry_form'),
    path('submit_inquiry/', views.submit_inquiry, name='submit_inquiry'),
    path('plantrip/', views.plantrip, name='plantrip'),  # Main PlanTrip Page
    path('career/', views.career, name='career'),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Django AllAuth URLs


    path("login/", views.login_view, name="login"),  # Define 'login' URL


    # 📌 Individual PlanTrip Destination Pages
    path('plantrip/adventure/', views.adventure, name='adventure'),
    path('plantrip/spiritual/', views.spiritual, name='spiritual'),
    path('plantrip/mountains/', views.mountains, name='mountains'),
    path('plantrip/heritage/', views.heritage, name='heritage'),
    path('plantrip/honeymoon/', views.honeymoon, name='honeymoon'),
    path('plantrip/weekend/', views.weekend, name='weekend'),
    path('plantrip/romantic/', views.romantic, name='romantic'),
    path('plantrip/pilgrimage/', views.pilgrimage, name='pilgrimage'),
    path('plantrip/foodie/', views.foodie, name='foodie'),
    path('plantrip/trekking/', views.trekking, name='trekking'),
    path('plantrip/relax/', views.relax, name='relax'),
    path('plantrip/international/', views.international, name='international'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
