from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render(request,'student/index.html')

def submit(request):
    name=request.POST.get('name')
    context={}
    context['name']=name
    return render(request, 'student/index.html',context)

from student.forms import reg
def register(request):
    form =reg()
    context={}
    context['form']=form
    if request.method=='POST':
        form=reg(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            print(name)
            context={}
            context['name']=name
            return render(request, 'student/register.html', context)
    return render(request,'student/register.html',context)


