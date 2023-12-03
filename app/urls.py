from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('', views.home),
    # path('student', views.student_list),
    # path('stu/<int:pk>/', views.student_detail),
    # path('student/', views.StudentList.as_view()),
    # path('studentdetail/<int:pk>/', views.StudentDetail.as_view()),
    path('studentlist/', views.StudentList.as_view()),
    path('studentdetail/<int:pk>/', views.StudentDetail.as_view()),
]

