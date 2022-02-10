from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    user_info=False
    if request.method=='POST':
        user_name=request.POST.get('user') 
        url='https://api.github.com/users/'+str(user_name)
        response=requests.get(url)
        user_info=response.json()  
    return render(request,'index.html',context={'user_info':user_info})