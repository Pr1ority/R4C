from django.urls import path

from . import views

urlpatterns = [
    path('add-robot/', views.add_robot, name='add-robot'),
]
