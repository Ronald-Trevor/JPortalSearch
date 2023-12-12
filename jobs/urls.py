from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/add/', views.addjob, name='addjob'),
    path('jobs/', views.jobs, name='jobs'),
    path('job/details/<int:id>/', views.jobdetails, name='jobdetails')
]