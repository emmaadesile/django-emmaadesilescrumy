from django.contrib import admin
from .models import ScrumyUser, ScrumyGoals, GoalStatus

# Register your models here.
myModels = [ScrumyUser, ScrumyGoals, GoalStatus]
admin.site.register(myModels)

