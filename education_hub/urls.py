from django.urls import path
from . import views

# handler404 = 'views.error_404'

urlpatterns = [
    path('', views.index),
    path('courses/', views.courses),
    path('about/', views.about),
    path('coursesDtails/', views.coursesDtails),
    path('contact/', views.contact),
    path('login/', views.login),
    path('register/', views.register),
    path('Spannel/', views.Spannel),
    path('Tpannel/', views.Tpannel)
]