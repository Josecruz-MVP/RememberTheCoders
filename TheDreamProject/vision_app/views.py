
# Create your views here.
from django.shortcuts import render, redirect
from django.views import View

#from django.views import Task
from vision_app.models import Vision,Goal,Task
from django.views.generic.list import ListView
from vision_app.forms import VisionForm

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
    
    def post(self,request):
       if 'save_vision' in request.POST:
        Vision_Form = VisionForm(request.POST)
        print(Vision_Form.is_valid())
        if Vision_Form.is_valid():
          Vision_Form.save()
        return render(request,'add_vision.html')



class AddGoalTask(View): 
    def get(self, request):
        return render(request, 'addgoaltask.html')