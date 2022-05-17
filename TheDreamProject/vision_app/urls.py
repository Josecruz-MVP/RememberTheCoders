from django.urls import path

from vision_app.views import Homepage, Addvision,VisionListView

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('addvision/', Addvision.as_view(), name='AddVision'),
    path('Dashboard/', VisionListView.as_view(), name='article-list')
]

