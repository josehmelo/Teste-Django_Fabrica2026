from django.urls import path
from . import views

urlpatterns = [
    path = ('', views.ViacepListView.as_view(), name='form'),
]