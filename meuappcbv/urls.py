from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViaCepView.as_view(), name='form'),
  
]