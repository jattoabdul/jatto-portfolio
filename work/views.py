from django.shortcuts import render, get_object_or_404
from work.models import Client, Medium, Project
from django.shortcuts import redirect


# Create your views here.
def work(request):
    medium = Medium.objects.all()
    project = Project.objects.all()
    context_dict = {'medium': medium, 'project': project}
    return render(request, 'portfolio/portfolio.html', context=context_dict)
