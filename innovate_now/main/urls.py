from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

    
    path('service/list/', views.service_list, name='service_list'),
    path('service/create/', views.service_create, name='service_create'),
    path('service/update/<int:pk>/', views.service_update, name='service_update'),
    path('service/delete/<int:pk>/', views.service_delete, name='service_delete'),
]
