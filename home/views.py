#coding:utf-8

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    #my_str = u"你好我是文凱"
    my_list = ["你", "我", "他"]
    return render(request, 'index.html', {'my_list': my_list})
    #return HttpResponse(u"我是KENNY")

    
def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a) + int(b)
    return HttpResponse(str(c));
    

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    