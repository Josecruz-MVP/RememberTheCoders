from django.urls import path
from vision_app.views import Homepage, Addvision,VisionListView,AddGoalTask

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('addvision/', Addvision.as_view(), name='AddVision'),
    path('addgoaltask/', AddGoalTask.as_view(), name='AddGoalTask'),
    path('Dashboard/', VisionListView.as_view())
    ]

