from django.urls import path

from . import views

urlpatterns = [
    path(
        'weekly-summary/',
        views.download_weekly_summary,
        name='weekly-summary'
    ),
]
