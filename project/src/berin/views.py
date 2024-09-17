from django.utils import timezone
from django.views import generic
from django.views.generic.list import ListView
from django.shortcuts import render

from src.berin.models import Project, Talk


class TalkListView(ListView):
    template_name = 'berin/talks.html'
    model = Talk
    context_object_name = 'talks'

class ProjectListView(ListView):
    template_name = 'berin/projects.html'
    model = Project
    context_object_name = 'projects'

class ProjectDetailView(generic.DetailView):
    template_name = 'berin/project_detail.html'
    model = Project
    context_object_name = 'project'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

