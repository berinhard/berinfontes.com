from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from src.berin.views import TalkListView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^projects/$', TemplateView.as_view(template_name='projects.html'), name='projects'),
    url(r'^talks/$', TalkListView.as_view(), name='talks'),
    url(r'^links/$', TemplateView.as_view(template_name='links.html'), name='links'),
    prefix_default_language=True,
)

if not settings.PRODUCTION:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
