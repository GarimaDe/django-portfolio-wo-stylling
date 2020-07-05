from django.shortcuts import render
from .models import Project

# Create your views here.
def Home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_ex/home.html', {'projects': projects}) 