from django.contrib import admin
from jatto.models import About, AboutFeed, Skill, ResumeStudyPlace, ResumeWorkPlace


class AboutAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class AboutFeedAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_position', 'client_company')
    search_fields = ('client_company', 'client_name')


class ResumeStudyPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_year', 'end_year')
    search_fields = ('name', 'start_year', 'end_year')


class ResumeWorkPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_year', 'end_year')
    search_fields = ('name', 'start_year', 'end_year')


# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(AboutFeed, AboutFeedAdmin)
admin.site.register(Skill)
admin.site.register(ResumeStudyPlace, ResumeStudyPlaceAdmin)
admin.site.register(ResumeWorkPlace, ResumeWorkPlaceAdmin)
