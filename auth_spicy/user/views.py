from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def User(request):
	return render(request, 'home.html')

def Register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {
	'form':form,
	}
	return render(request, 'register.html', context)
def LoginForm(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')

	context = {}
	
	return render(request, 'index.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')