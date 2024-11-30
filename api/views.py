# client_service_website/views.py

from django.shortcuts import render, redirect
import os, json
from pathlib import Path
# Login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Debugging statement
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")  # Redirect to login page after successful registration
        else:
            print("Form errors:", form.errors)  # Debugging statement
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "register.html", context)

# Login View
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to homepage or dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Protected Page Example
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def homepage(request):
    if request.user.is_authenticated:   
        return render(request, 'homepage.html')  # Render a homepage template

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    featured, others = load_projects()
    return render(request, 'projects.html', {
        "featured_projects" : featured,
        "other_projects": others,
        "carasoul_indicators": [f"{i}" for i in range(1, len(featured))]
    })

def testimonials(request):
    data = load_testimonials()
    return render(request, 'testimonials.html', {
        "testimonials" : data
    })

def contact(request):
    return render(request, 'contact.html')




### Helper Functions
def load_projects():
    directory = "api/static/data/projects/"
    featured = []
    others = []

    # Parent Folder has 2 subfolders - featured, others
    for subfolder in ["featured", "others"]:
        p = Path(directory)/ subfolder
        project_folder_paths = [
            Path(p)/item for item in os.listdir(p) if (Path(p) / item).is_dir()
        ]
        for folder_path in project_folder_paths:
            # Each project folder has 2 files - .json metadata and image
            folder_files = os.listdir(folder_path)
            project_data = {}

            for file in folder_files:
                file_path = folder_path / file
                if file.endswith(".json"):
                    with open(file_path, "r") as d:
                        project_data = json.load(d)
                else:
                    image_path = file_path.relative_to(Path("api/static"))
                
            project_data["image_path"] = f"/static/{image_path}"
            if subfolder == "featured":
                featured.append(project_data)
            else:
                others.append(project_data)
    
    return featured, others


def load_testimonials():
    directory = "api/static/data/testimonials/"
    testimonial_dirs = [
        Path(directory) / item for item in os.listdir(directory)
        if (Path(directory) / item).is_dir()
    ]
    
    testimonial_data = []
    for dir in testimonial_dirs:
        files = os.listdir(dir)
        data = {}

        for file in files:
            file_path = dir / file

            if file.endswith(".json"):
                with open(file_path, 'r') as d:
                    data = json.load(d)
            else:
                # Convert image path to URL-friendly format
                image_path = file_path.relative_to(Path("api/static"))

        # Add the relative image path to the data dictionary
        data["image_path"] = f"/static/{image_path}"
        testimonial_data.append(data)
    
    return testimonial_data