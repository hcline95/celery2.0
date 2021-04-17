from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("tasks/<int:page>", views.tasks, name="tasks"),
    path('check', views.check_task_status, name='check_task_status')
]
