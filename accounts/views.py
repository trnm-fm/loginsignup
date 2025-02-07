from django.shortcuts import render , HttpResponse , redirect
from .forms import CustomUserCreationForm
# Create your views here.

def welcome(request):
    return HttpResponse('<h1>welcome</h1>')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})
