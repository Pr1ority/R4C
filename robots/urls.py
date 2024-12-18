from django.urls import path

from . import views

urlpatterns = [
    path('add-robot/', views.add_robot, name='add-robot'),
    path(
        'weekly-summary/',
        views.download_weekly_summary,
        name='weekly-summary'
    ),
]
