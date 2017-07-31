from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext
from cmdb import models

# Create your views here.
user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]


def index(request):
    #return HttpResponse("hello world , django!")
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        #print(username,password)
        #temp={"user":username,"pwd":password}
        #user_list.append(temp)
        #添加到数据库中
        models.UserInfo.objects.create(user=username,pwd=password)
    #读取数据表中的所有数据
    user_list=models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})