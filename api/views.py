# client_service_website/views.py

from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')  # Render a homepage template

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')