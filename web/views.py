from django.shortcuts import render

# Create your views here.

def web(request):
    return render(request,'static/web/html/index.html')

