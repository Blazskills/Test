from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

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