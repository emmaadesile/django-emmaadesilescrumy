from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class ScrumyUser(models.Model):
  username = models.CharField(max_length=50, blank=True, null=False)
  email = models.EmailField(max_length=100, blank=True, null=False)
  ROLE = (
    ('O', 'Owner'),
    ('A', 'Admin'),
    ('QA', 'Quality Analyst'),
    ('D', 'Developer'),
  )
  role = models.CharField(max_length=50, choices=ROLE, default='O')

  def __str__(self):
    return self.username

  class Meta:
    verbose_name_plural = 'ScrumyUser'

class GoalStatus(models.Model):
  STATUS = (
    ('WT', 'Weekly Task'),
    ('DT', 'Daily Task'),
    ('V', 'Verified'),
    ('D', 'Done')
  )

  status = models.CharField(max_length=50, choices=STATUS, default='DT', null=False)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = 'GoalStatus'
  
class ScrumyGoals(models.Model):
  user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
  status_id = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
  task_title = models.CharField(max_length=200, blank=True, null=False)
  # task_id = models.IntegerField(default=10, null=False)
  task = models.TextField(blank=True, null=False)
  created_at = models.DateTimeField(default=timezone.now, null=False)
  updated_at = models.DateTimeField(default=timezone.now, null=False)

  def __str__(self):
    return self.task_title

  class Meta:
    verbose_name_plural = 'ScrumyGoals'
