
#Create your views here.
from django.shortcuts import render
from django.views import View

from django.views.generic.list import ListView

from .forms import VisionForm, GoalForm, TaskForm
from .models import Vision,Goal,Task

# Create your views here.

class Homepage(View):
    def get(self, request):
        return render(request, 'home.html')



'''Vision'''
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


'''Vision'''
class VisionListView(ListView):
    model: Vision
    def get(self, request,):
         vision = Vision.objects.all()
         form = VisionForm()
        
       
         return render(
             request=request,
             template_name='addgoaltask.html',
             context={'visionname': vision,
             'vision_form' : form
             }
         )

    def post(self, request):
        form = VisionForm(request.POST)
        form.save()

        if form.is_valid():
              name_vision = form.cleaned_data['vision_name']
              Vision.objects.create(vision_name=name_vision)
              

        return render(request, 'addgoaltask.html',{
                'Vision_Form' : VisionForm,
            })

       
   
'''Goal'''
class AddGoalTask(View): 
    def get(self, request):
        Goal_Form = GoalForm()
        
        return render(request, 'addgoaltask.html',{
                '   Goal_Form' : Goal_Form,
            })       
    
   

#Goal list view here.
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










        
         

