from django.contrib import admin
from apps.projects.models import Project, Document


class DocumentInline(admin.StackedInline):
    model = Document
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]


admin.site.register(Project, ProjectAdmin)

