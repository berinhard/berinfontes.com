from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from src.berin.views import ProjectListView, TalkListView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^projects/$', ProjectListView.as_view(), name='projects'),
    url(r'^projects/python-brasil-badges-visualizations$', TemplateView.as_view(template_name='projects/pybr_proj.html'), name='pybr_badge'),
    url(r'^projects/invisible-movements', TemplateView.as_view(template_name='projects/mov-invisiveis.html'), name='invisible_mov'),
    url(r'^projects/exch-with-turkers', TemplateView.as_view(template_name='projects/turkers.html'), name='exch_turkers'),
    url(r'^talks/$', TalkListView.as_view(), name='talks'),
    url(r'^links/$', TemplateView.as_view(template_name='links.html'), name='links'),
    prefix_default_language=True,
)

if not settings.PRODUCTION:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
