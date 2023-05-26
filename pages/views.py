from django.shortcuts import render

from .models import Login

# Create your views here.

def index(request):
    username =request.POST.get('username')
    password =request.POST.get('password')
    data = Login(username = username , password = password)
    
    if request.method == 'POST':
        data.save()
       
    return render(request, 'pages/index.html')
