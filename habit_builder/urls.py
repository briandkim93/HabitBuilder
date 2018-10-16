from decouple import config

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('account.urls')),
    path('habits/', include('habit.urls')),
    path(config('ADMIN_URL'), admin.site.urls)
]
