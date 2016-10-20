from django.contrib import admin
from work.models import Client, Medium, Project


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'project_url', 'completion_date', 'client', 'in_development', 'is_public']


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']


class MediumAdmin(admin.ModelAdmin):
    search_fields = ['name']

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Medium, MediumAdmin)
