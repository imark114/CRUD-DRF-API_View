from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentApi/', views.student_api),
    path('studentApi/<int:pk>/', views.student_api),
]
