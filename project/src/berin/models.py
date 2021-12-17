from django.db import models
from markupfield.fields import MarkupField


class Talk(models.Model):
    year = models.IntegerField()
    event = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=280)
    presentation_link = models.URLField()
    video_link = models.URLField(default='', blank=True)
    interview_link = models.URLField(default='', blank=True)
    conference_link = models.URLField(default='', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def links(self):
        links = [
            ('Presentation', self.presentation_link),
            ('Video', self.video_link),
            ('Interview', self.interview_link),
            ('Streaming', self.conference_link),
        ]
        return [(t, l) for t, l in links if l]

    class Meta:
        ordering = ['-date_added']

class Project(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = MarkupField(default_markup_type='markdown')
    short_description = models.CharField(max_length=140)
    image = models.ImageField(upload_to='projectcovers', verbose_name='Capa')
    slug = models.SlugField(primary_key=True)
    html_extra = models.TextField(default='', blank=True)

    class Meta: 
        ordering = ['-year']

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projectimages')
    short_description = models.CharField(max_length=140, default='', blank=True)