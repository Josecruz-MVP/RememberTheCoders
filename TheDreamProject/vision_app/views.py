#Create your views here.
from django.shortcuts import render
from django.views import View

from django.views.generic.list import ListView

from .forms import VisionForm
from .models import Vision,Goal,Task

# Create your views here.
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


class Homepage(View):
    def get(self, request):
        return render(request, 'home.html')

class Addvision(View):
    def get(self, request):
        Vision_Form = VisionForm()
        return render(request, 'add_vision.html',{
                'Vision_Form' : Vision_Form,
            })
    def post(self,request):
        '''POST the data in the form submitted by the user, creating a new task in the todo list'''
        Vision_Form = VisionForm(request.POST)
        Vision_Form.save()
        return render(request,'add_vision.html')

class AddGoalTask(View): 
    def get(self, request):
        return render(request, 'addgoaltask.html',{
                '   Goal_Form' : Goal_Form,
            },{
                'Task_Form' : Task_Form,
            })
    
    def post(self,request):
        '''POST the data in the form submitted by the user, creating a new task in the todo list'''
        Goal_Form = GoalForm(request.POST)
        Goal_Form.save()
        Task_Form = TaskForm(request.POST)
        Task_Form.save()
        return render(request,'addgoaltask.html')