from django.urls import path

from vision_app.views import Homepage

urlpatterns = [
    # paintapp/
    path('', Homepage.as_view(), name='Home'),
]