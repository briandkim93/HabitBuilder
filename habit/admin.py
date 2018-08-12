from django.contrib import admin

from .models import Day
from .models import DateCompleted
from .models import Habit

# Register your models here.
admin.site.register(Day)
admin.site.register(DateCompleted)
admin.site.register(Habit)