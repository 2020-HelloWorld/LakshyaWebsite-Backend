from django.contrib import admin
from django.urls import path
from internships.views import internship_list_view, internship_detail_view, internship_add_view

urlpatterns = [
    path('internships/', internship_list_view, name='internship_list'),
    path('internships/detail/', internship_detail_view, name='internship_detail'),
    path('internships/add/', internship_add_view, name='add_internship')
]
