from django.shortcuts import render

# Create your views here.

def page(request):
    return render(request,'calc/calculation.html')

def res(request):
    num1=int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    result=num1+num2
    context={}
    context['res']=result
    return render(request,'calc/calculation.html',context)

