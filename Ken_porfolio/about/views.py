from django.shortcuts import render
from about.models import About
# Create your views here.

def About_index(request):
    about = About.objects.all()
    context = {
        "about": about
    }
    return render(request, "About_index.html",context)