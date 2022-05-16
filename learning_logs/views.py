from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from learning_logs.models import Topic


def index(request):
    print('666')
    return render(request,'learning_logs/index.html')
def topics(request):
    # 显示所有主体
    topics = Topic.objects.order_by('data_added')
    context = {'topics':topics}

    return  render(request,'learning_logs/topics.html',context)
