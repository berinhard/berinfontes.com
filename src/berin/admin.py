from django.contrib import admin

from src.berin.models import Talk


class TalkAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'year']


# Register your models here.
admin.site.register(Talk, TalkAdmin)
