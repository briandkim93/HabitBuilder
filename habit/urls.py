from django.urls import path

from . import views

urlpatterns = [
    path('day/<slug:date_slug>/', views.day, name='day'),
    path('manage/', views.manage, name='manage')
]