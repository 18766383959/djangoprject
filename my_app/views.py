from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('轮哥网站')
def add(request):
    x=request.GET.get("x")
    y=request.GET.get("y")
    if not x or y:
        return HttpResponse('查看参数')
    return HttpResponse(int(x)+int(y))