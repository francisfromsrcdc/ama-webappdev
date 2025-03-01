from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the home page
def home(request):
    return render(request, 'home.html')

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    # Render the registration page template (GET request)
    return render(request, 'register.html')

# Create a new Todo
def create_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        Todo.objects.create(task=task)
        return redirect('list_todos')
    return render(request, 'todo/create_todo.html')

# List all Todos
def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list_todos.html', {'todos': todos})

# Update a Todo
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.task = request.POST['task']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('list_todos')
    return render(request, 'todo/update_todo.html', {'todo': todo})

# Delete a Todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')