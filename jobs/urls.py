from django.contrib import admin
from django.urls import path
from jobs.views import job_list_view

urlpatterns = [
    path('jobs/', job_list_view, name='job_list')
    # path('jobs/detail/', job_detail_view, name='job_detail'),
    # path('jobs/add/', add_job_view, name='add_job'),
]