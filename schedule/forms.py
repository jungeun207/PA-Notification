from django import forms
from .models import AssessmentSchedule

class AssessmentScheduleForm(forms.ModelForm):
    class Meta:
        model = AssessmentSchedule
        fields = ['grade', 'title', 'description', 'date']
        labels = {
            'grade': '학년',
            'title': '제목',
            'description': '부가 설명',
            'date': '날짜(yyyy-mm-dd)',
        }
