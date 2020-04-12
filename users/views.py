from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
	if request.method == 'POST':
		# create a form through django get the input data 
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('blog_home_page')
	else:
		form=UserRegistrationForm()
	return render(request,'users/register.html',{'form':form})

# Create your views here.
