from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('getSubcategory_agric/', views.get_subcategory_agric, name='getSubcategory_agric'),
    path('getSubcategory_log/', views.get_subcategory_log, name='getSubcategory_log'),
    path('getSubcategory_mer/', views.get_subcategory_mer, name='getSubcategory_mer')
]

urlpatterns += staticfiles_urlpatterns()