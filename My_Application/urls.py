from django.urls import path
from . import views  # Import views from the current application
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

def home_view(request):
    return render(request, 'RoleSelection.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('RoleSelection.html', views.RoleSelection, name='RoleSelection'),
      path('userlogin.html', views.userlogin, name='userlogin'),
      path('adminlogin.html', views.adminlogin, name='adminlogin'),
      path('Register.html', views.register, name='Register'),
      
    path('user.html', views.user_profile, name='user_profile'),
     path('venue.html', views.venue, name='venue'),
      path('photography.html', views.photography, name='photography'),
       path('accessories.html', views.accessories, name='accessories'),
        path('vehicle.html', views.vehicle, name='vehicle'),
         path('accommodation.html', views.accommodation, name='accommodation'),
         path('forms.html', views.forms, name='forms'),

    path('admin.html', views.admin_view, name='admin_view'),
    path('user', views.user_view, name='user'),
    path('submit_event_request/', views.submit_event_request, name='submit_event_request'),
     path('submit_venue_form/', views.submit_venue_form, name='submit_venue_form'),
      path('submit_photography_form/', views.submit_photography_form, name='submit_photography_form'),
      path('submit_accessories_form/', views.submit_accessories_form, name='submit_accessories_form'),
       path('submit_vehicle_form/', views.submit_vehicle_form, name='submit_vehicle_form'),
           path('submit_accommodation_form/', views.submit_accommodation_form, name='submit_accommodation_form'),
 path('register_user/', views.register_user, name='register_user'),
 path('login_user/', views.login_user, name='login_user'),
    path('admin_event_list', views.admin_event_list, name='admin_event_list'),
 path('admin/events/approve/<int:event_id>/', views.approve_event, name='approve_event'),
    path('admin/events/reject/<int:event_id>/', views.reject_event, name='reject_event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
