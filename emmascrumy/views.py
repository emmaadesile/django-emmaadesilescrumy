from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyUser, ScrumyGoals, GoalStatus

# Create your views here.
def index(request):
  scrumy_goals = ScrumyGoals.objects.all()
  goal_output = ', '.join([s.task for s in scrumy_goals])
  daily_goal_status = GoalStatus.objects.filter(status='DT')
  daily_goal_status_output = ', '.join([t.status for t in daily_goal_status])
  return HttpResponse('These are the scrumy goals: ' + goal_output + '. ' + 'These are the daily tasks: ' + daily_goal_status_output)

def move_goal(request, task_id):
  return HttpResponse('This is the move task view')

def add_task(request, task_id):
  goal = ScrumyGoals.objects.get(id=task_id)
  return HttpResponse(goal.task)

def add_user(request):
  return HttpResponse('Add user view')