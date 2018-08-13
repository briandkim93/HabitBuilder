from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta

from .models import Day
from .models import Habit

# Create your views here.
@login_required(login_url='/')
def day(request, date_slug):
    date_obj = date.fromisoformat(date_slug)
    day_int = date_obj.weekday()
    day_str = ''
    if day_int == 0:
        day_str = 'Monday'
        day_str_abbr = 'mon'
    elif day_int == 1:
        day_str = 'Tuesday'
        day_str_abbr = 'tue'
    elif day_int == 2:
        day_str = 'Wednesday'
        day_str_abbr = 'wed'
    elif day_int == 3:
        day_str = 'Thursday'
        day_str_abbr = 'thu'
    elif day_int == 4:
        day_str = 'Friday'
        day_str_abbr = 'fri'
    elif day_int == 5:
        day_str = 'Saturday'
        day_str_abbr = 'sat'
    elif day_int == 6:
        day_str = 'Sunday'
        day_str_abbr = 'sun'
    prev_date_slug = str(date_obj - timedelta(days=1))
    next_date_slug = str(date_obj + timedelta(days=1))
    habit_details = []
    for habit in Habit.objects.filter(user__username=request.user.username):
        days = []
        for day in habit.days.all():
            days += [day.day]
        should_display = habit.date_created <= date_obj
        habit_details += [[habit.id, habit.habit, days, should_display]]
    context = {
        'date': date_slug,
        'day_str': day_str,
        'day_str_abbr': day_str_abbr,
        'prev_date_slug': prev_date_slug,
        'next_date_slug': next_date_slug,
        'habit_details': habit_details
    }
    return render(request, 'habit/day.html', context)

@login_required(login_url='/')
def manage(request):
    if request.method == 'POST':
        if request.POST['submit'] == 'Add Habit':
            habit = request.POST['habit']
            days = request.POST.getlist('days')
            context = {
                'habit': habit,
                'error': ''
            }
            if not habit:
                context['error'] == 'Please enter a habit name'
                return render(request, 'habit/manage.html', context)
            if len(days) == 0:
                context['error'] == 'Please select the days that this habit is to be completed'
                return render(request, 'habit/manage.html', context)
            new_habit = Habit()
            new_habit.habit = habit
            new_habit.user = request.user
            new_habit.date_created = timezone.localdate()
            new_habit.save()
            for day in days:
                new_day = Day.objects.get(day=day)
                new_habit.days.add(new_day)
            new_habit.save()
            return redirect('manage')
        else:
            habit_id = request.POST['remove']
            habit = Habit.objects.get(id=habit_id)
            habit.delete()
            return redirect('manage')
    else:
        habit_details = []
        for habit in Habit.objects.filter(user__username=request.user.username):
            days = []
            for day in habit.days.all():
                days += [day.day]
            habit_details += [[habit.id, habit.habit, days]]
        context = {
            'habit_details': habit_details,
        }
        return render(request, 'habit/manage.html', context)