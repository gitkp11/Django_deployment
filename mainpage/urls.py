from django.urls import path
from .views import ProjectListAndFormView, allProjectsView

app_name = 'mainpage'

urlpatterns = [
    path('', ProjectListAndFormView.as_view(), name='main'),
    path('projects', allProjectsView.as_view(), name='allprojects'),
]
