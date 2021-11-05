from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render

from src.berin.models import Project, Talk


class TalkListView(ListView):
    template_name = 'berin/talks.html'
    model = Talk
    context_object_name = 'talks'

##### changes

class ProjectListView(ListView):
    template_name = 'berin/projects.html'
    model = Project
    context_object_name = 'projects'
