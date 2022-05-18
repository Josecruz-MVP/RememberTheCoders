from django.urls import path

from vision_app.views import Homepage, Addvision,VisionListView,GoalListView,TaskListView

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('addvision/', Addvision.as_view(), name='AddVision'),
    path('Dashboard/', VisionListView.as_view()),
    path('goal/', GoalListView.as_view()),
    path('task/', TaskListView.as_view()),
]

