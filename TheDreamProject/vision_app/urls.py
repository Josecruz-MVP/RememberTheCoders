from django.urls import path


from vision_app.views import Homepage, Addvision, AddGoalTask, VisionListView, GoalListView

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('addvision/', Addvision.as_view(), name='AddVision'),
    path('addgoaltask/', AddGoalTask.as_view(), name='addgoaltaskview'),
    path('listvision/', VisionListView.as_view(), name='add_vision'),
    path('dashboard/', GoalListView.as_view(), name='dashboard')

]

