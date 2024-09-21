from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from account.forms.forms import LoginForm
from .decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:index')  
            else:
                messages.warning(request, 'Invalid email or password') 
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



@login_required
def accountlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('account:login')
