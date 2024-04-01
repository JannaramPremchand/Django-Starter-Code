from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home_view(request):
    # Sample data to pass to the template
    context = {
        'message': 'Welcome to our website!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    # Render the template with the provided data
    return render(request, 'core_templates/index.html', context)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or some other URL
            return redirect('home')
        else:
            # Return an invalid login error message
            return render(request, 'signin.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'auths_templates/signin.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or some other URL
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auths_templates/signup.html', {'form': form})