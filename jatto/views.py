from django.shortcuts import render
from jatto.models import About
from jatto.models import Skill
from jatto.models import ResumeStudyPlace
from jatto.models import ResumeWorkPlace
from jatto.models import AboutFeed


def index(request):
    home = About.objects.get(first_name='Aminujatto')
    context_dict = {'name': home}
    return render(request, 'jatto/index.html', context=context_dict)


def about(request):
    aboutme = About.objects.get(first_name='Aminujatto')
    skills = Skill.objects.all()
    context_dict = {'name': aboutme, 'skills': skills}
    return render(request, 'jatto/about.html', context=context_dict)


def resume(request):
    workresume = ResumeWorkPlace.objects.all()
    studyresume = ResumeStudyPlace.objects.all()
    feeds = AboutFeed.objects.all()
    context_dict = {'schools': studyresume, 'works': workresume, 'feeds': feeds}
    return render(request, 'jatto/resume.html', context=context_dict)



