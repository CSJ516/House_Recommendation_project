from django.urls import path
from . import views
# Create your tests here.
app_name = 'house'

urlpatterns = [
    path('solution', views.solution, name='solution'),
 
]