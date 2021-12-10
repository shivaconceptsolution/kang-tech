from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"swap/index.html")

def swaplogic(request):
    a = request.POST["txt1"]
    b = request.POST["txt2"]
    a,b = b,a
    return HttpResponse("a= "+str(a)+"b= "+str(b))	


