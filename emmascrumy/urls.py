from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add_task/<int:task_id>', views.add_task, name='add_task'),
  path('add_user/', views.add_user, name='add_user'),
]