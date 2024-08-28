from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="welcome"),  # Points to index.html
    path('random-image/<str:folder_name>/', random_image_view, name='random_image'),
    path('management/', views.management, name="management"),
    path('services/', views.services, name="services"),
    path('collaborations/', views.collaborations, name="collaborations"),
    path('contact/', views.contact, name="contact"),
    path('team/', views.team, name="team"),
    
    # # Authentication-related views
    # path('signup/', signup_view, name='signup'),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
]
