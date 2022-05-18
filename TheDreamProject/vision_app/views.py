
# Create your views here.
from django.shortcuts import render
from django.views import View

#from django.views import Task
from vision_app.models import Vision,Goal,Task
from django.views.generic.list import ListView

class VisionListView(ListView):

    model = Vision
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      #  context['now'] = timezone.now()
        return context

class GoalListView(ListView):

    model = Goal
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      #  context['now'] = timezone.now()
        return context

class TaskListView(ListView):

    model = Task
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      #  context['now'] = timezone.now()
        return context



# Create your views here.
class Homepage(View):
    def get(self, request):
        return render(request, 'home.html')

class Addvision(View):
    def get(self, request):
        return render(request, 'add_vision.html')

class AddGoalTask(View): 
    def get(self, request):
        return render(request, 'addgoaltask.html')