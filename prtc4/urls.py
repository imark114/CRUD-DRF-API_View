from django.contrib import admin
from django.urls import path
from student import views
from teacher.views import TeacherApiView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentApi/', views.student_api),
    path('studentApi/<int:pk>/', views.student_api),
    path('teacherApi/', TeacherApiView.as_view()),
    path('teacherApi/<int:pk>/', TeacherApiView.as_view()),
]
