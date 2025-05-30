from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Welcome, {username}. Your account has been successfully created.")
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()
#     return render (request,'users/register.html', {'form':form})
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            print(f"Created user: {user}")  # Debug line
            messages.success(request, f"Welcome, {username}. Your account has been successfully created.")
            return redirect('login')
        else:
            print(form.errors)  
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html', )
