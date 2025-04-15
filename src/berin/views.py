from django.utils import timezone
from django.views.generic.list import ListView

from src.berin.models import Talk


class TalkListView(ListView):
    template_name = 'berin/talks.html'
    model = Talk
    context_object_name = 'talks'
