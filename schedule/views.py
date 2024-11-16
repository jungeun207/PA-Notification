from django.shortcuts import render, redirect
from .models import Schedule
from .models import AssessmentSchedule
from .forms import AssessmentScheduleForm
from django.http import Http404
import calendar
from datetime import datetime

def assessment_add(request):
    if request.method == "POST":
        form = AssessmentScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_selection')
    else:
        form = AssessmentScheduleForm()

    return render(request, 'schedule/assessment_add.html', {'form': form})

def grade_selection(request):
    return render(request, 'schedule/grade_selection.html')

def delete_schedule(request, schedule_id):
    schedule = AssessmentSchedule.objects.get(id=schedule_id)
    schedule.delete()
    return redirect('calendar_view', grade=schedule.grade)

def calendar_view(request, grade):
    current_date = datetime.now()
    month_days = calendar.monthcalendar(current_date.year, current_date.month)  # 현재 월의 날짜들
    schedules = AssessmentSchedule.objects.filter(grade=grade, date__month=current_date.month)

    form = None
    if request.method == 'POST':
        form = AssessmentScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view', grade=grade)  # 새 일정 추가 후 리다이렉션
        
    year=2024
    month=11
    cal = calendar.Calendar(firstweekday=-1)
    month_days = cal.monthdayscalendar(year, month)
    
    context = {
        'grade': grade,
        'calendar': month_days,  # 달력 데이터
        'schedules': schedules,  # 해당 학년의 일정
        'form': form,
    }

    return render(request, 'schedule/calendar_view.html', context)
