from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('contacts/',views.contacts),
    path('about-us',views.about),
    path('tasks',views.tasks)
]