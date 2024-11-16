from django.db import models
from django.utils import timezone
from datetime import date

class Schedule(models.Model):
    title = models.CharField(max_length=100)  # 수행평가 제목
    date = models.DateField()  # 수행평가 날짜

    def __str__(self):
        return f"{self.date} - {self.title}"
    
'''class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    grade = models.IntegerField()
    
    def __str__(self):
        return self.title'''

class AssessmentSchedule(models.Model):
    grade = models.IntegerField(choices=[(1, '1학년'), (2, '2학년'), (3, '3학년')])
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.date})"