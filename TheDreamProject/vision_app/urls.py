from django.urls import path

from vision_app.views import Homepage, Addvision

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('addvision/', Addvision.as_view(), name='AddVision')
]