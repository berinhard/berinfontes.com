from django.contrib import admin

from src.berin.models import ProjectImage, Talk, Project

class ProjectImageInline(admin.StackedInline):
    model = ProjectImage

class TalkAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'year']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'year', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]



# Register your models here.
admin.site.register(Talk, TalkAdmin)
admin.site.register(Project, ProjectAdmin)
