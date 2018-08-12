from django.contrib import admin
from django.urls import path, include

from habit_builder.confidential import ADMIN_URL

urlpatterns = [
    path('', include('account.urls')),
    path('habits/', include('habit.urls')),
    path(ADMIN_URL, admin.site.urls)
]
