from django.shortcuts import render

def my_view_home(request):
    people = [
        {'name': 'A', 'age': 22},
        {'name': 'B', 'age': 32},
        {'name': 'C', 'age': 24},
    ]
    return render(request, 'header/index.html', context={'people': people})

def my_view_about(request):
    return render(request, 'about.html')  # Remove the leading slash

def my_view_project(request):
    return render(request, 'project.html')  # Remove the leading slash

def my_view_contact(request):
    return render(request, 'contact.html')  # Remove the leading slash
