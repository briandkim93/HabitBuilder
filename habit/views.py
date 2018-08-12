from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Day
from .models import Habit

# Create your views here.
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
            new_habit.date_created = timezone.datetime.now()
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
        for habit in Habit.objects.all():
            days = []
            for day in habit.days.all():
                days += [day.day]
            habit_details += [[habit.id, habit.habit, days]]
        context = {
            'habit_details': habit_details,
        }
        return render(request, 'habit/manage.html', context)