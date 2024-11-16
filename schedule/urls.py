from django.urls import path
from . import views

urlpatterns = [
    path('', views.grade_selection, name='grade_selection'),  # 학년 선택 페이지
    path('schedule/delete/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
    path('calendar/<int:grade>/', views.calendar_view, name='calendar_view'),
    path('assessment/add/', views.assessment_add, name='assessment_add'),  # 수행평가 추가 페이지 URL
]