from django.shortcuts import render

# Create your views here.

def jyothi(request):
    return render(request,'jyothi.html')


def kiran(request):
    return render(request,'kiran.html')


def vj(request):
    return render(request,'vj.html')

def fruit(request):
    return render(request,'fruit.html')
