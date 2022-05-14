
# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views import Task


# Create your views here.
class Homepage(View):
    def get(self, request):
        return render(request, 'home.html')

class Addvision(View):
    def get(self, request):
        return render(request, 'add_vision.html')

