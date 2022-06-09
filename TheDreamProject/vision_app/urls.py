from django.urls import path


from vision_app.views import Homepage, Addvision, AddGoalTask, VisionListView

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('addvision/', Addvision.as_view(), name='AddVision'),
    path('addgoaltask/', AddGoalTask.as_view(), name='AddGoalTask'),
    path('addgoaltask/', VisionListView.as_view(), name='add_vision')

]

