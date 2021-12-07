from django.urls import path
from backend.views import *

app_name = 'Backend'

urlpatterns = [
    path('students/', StudentListView.as_view()),
    path('students/create/', StudentCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('students/edit/<int:pk>/', StudentEditView.as_view()),
    path('instructors/', InstructorListView.as_view()),
    path('instructors/create/', InstructorCreateView.as_view()),
    path('instructors/<int:pk>/', InstructorDetailView.as_view()),
    path('group/', GroupListView.as_view()),
    path('group/create/', GroupCreateView.as_view()),
    path('schedule/', ScheduleListView.as_view()),
    path('schedule/create/', ScheduleCreateView.as_view()),
    path('schedule/<int:pk>/', ScheduleEditView.as_view()),
    path('student/schedule/', ScheduleStudentView.as_view()),
    path('instructor/schedule/', ScheduleInstructorView.as_view()),
    path('request/', RequestView.as_view()),
    path('request/<int:pk>/', RequestEditView.as_view()),
    path('status/', StatusListView.as_view()),
]
