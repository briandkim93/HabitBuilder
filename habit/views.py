from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta

from .models import Day
from .models import DateCompleted
from .models import Habit

# Create your views here.
@login_required(login_url='/')
def day(request, date_slug):
    date_obj = date.fromisoformat(date_slug)
    if request.method == 'POST':
        habit_id = request.POST['habit_id']
        if request.POST['submit'] == 'Done':
            habit_obj = Habit.objects.get(id=habit_id)
            try:
                date_completed_obj = DateCompleted.objects.get(date_completed=date_obj)
                habit_obj.dates_completed.add(date_completed_obj)
                habit_obj.save()
                return redirect('/habits/day/' + date_slug)
            except DateCompleted.DoesNotExist:
                new_date_completed = DateCompleted()
                new_date_completed.date_completed = date_obj
                new_date_completed.save()
                habit_obj.dates_completed.add(new_date_completed)
                habit_obj.save()
                return redirect('/habits/day/' + date_slug)
        else:
            habit_obj = Habit.objects.get(id=habit_id)
            date_slug = request.POST['date_completed']
            date_obj = date.fromisoformat(date_slug)
            date_completed_obj = DateCompleted.objects.get(date_completed=date_obj)
            habit_obj.dates_completed.remove(date_completed_obj)
            habit_obj.save()
            return redirect('/habits/day/' + date_slug)
    else:
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
        formatted_date = date_obj.strftime("%B %d, %Y")
        prev_date_slug = str(date_obj - timedelta(days=1))
        next_date_slug = str(date_obj + timedelta(days=1))
        habit_details = []
        for habit_obj in Habit.objects.filter(user__username=request.user.username):
            days = []
            for day_obj in habit_obj.days.all():
                days += [day_obj.day]
            should_display = habit_obj.date_created <= date_obj
            habit_detail = {}
            habit_detail['id'] = habit_obj.id
            habit_detail['habit'] = habit_obj.habit
            habit_detail['days'] = days
            dates_completed = []
            dates_completed_objs = []
            for date_completed_obj in habit_obj.dates_completed.all():
                dates_completed_objs += [date_completed_obj.date_completed]
                dates_completed += [date_completed_obj.date_completed.isoformat()]
            days_in_a_row = 0
            if date_obj in dates_completed_objs:
                days_in_a_row = 1
                while (date_obj - timedelta(days=1)) in dates_completed_objs:
                    days_in_a_row += 1
                    date_obj = date_obj - timedelta(days=1)
            habit_detail['days_in_a_row'] = days_in_a_row
            habit_detail['dates_completed'] = dates_completed
            habit_detail['should_display'] = should_display
            habit_details += [habit_detail]
        displayed_habits_len = 0
        for habit_detail in habit_details:
            if habit_detail['should_display'] == True:
                displayed_habits_len += 1
        context = {
            'date_slug': date_slug,
            'formatted_date': formatted_date,
            'day_str': day_str,
            'day_str_abbr': day_str_abbr,
            'prev_date_slug': prev_date_slug,
            'next_date_slug': next_date_slug,
            'habit_details': habit_details,
            'displayed_habits_len': displayed_habits_len
        }
        return render(request, 'habit/day.html', context)

@login_required(login_url='/')
def manage(request):
    habit_details = []
    for index, habit_obj in enumerate(Habit.objects.filter(user__username=request.user.username)):
        days = []
        for day_obj in habit_obj.days.all():
            days += [day_obj.day.capitalize()]
        habit_detail = {}
        habit_detail['id'] = habit_obj.id
        habit_detail['habit'] = habit_obj.habit
        habit_detail['days'] = ', '.join(days)
        habit_details += [habit_detail]
    context = {
        'habit': '',
        'habit_details': habit_details,
    }
    if request.method == 'POST':
        if request.POST['submit'] == 'Add':
            habit = request.POST['habit']
            days = request.POST.getlist('days')
            context['habit'] = habit
            if not habit:
                return render(request, 'habit/manage.html', context)
            if len(days) == 0:
                return render(request, 'habit/manage.html', context)
            new_habit = Habit()
            new_habit.habit = habit
            new_habit.user = request.user
            new_habit.date_created = (datetime.now() - timedelta(hours=7)).date().isoformat()
            new_habit.save()
            for day in days:
                new_day = Day.objects.get(day=day)
                new_habit.days.add(new_day)
            new_habit.save()
            return redirect('manage')
        else:
            habit_id = request.POST['remove']
            habit_obj = Habit.objects.get(id=habit_id)
            habit_obj.delete()
            return redirect('manage')
    else:
        return render(request, 'habit/manage.html', context)