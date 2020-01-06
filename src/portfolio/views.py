from django.shortcuts import render
from about.models import Owner

def index(request):
    projects = Owner.objects.all()
    return render(request, 'index.html',{'projects': projects} )


def blog(request):
    return render(request, 'blog.html', {})

def features(request):
    return render(request, 'features.html', {})

def single_slider(request):
    return render(request, 'single-slider.html', {})

def single_video(request):
    return render(request, 'single-video.html', {})

def single(request):
    return render(request, 'single.html', {})