from django.shortcuts import render

# Create your views here.


# get method for stdlogn.html page
def login(request):
    return render(request,'student/studlogin.html')

# post method for studlogin.html
def display_details_in_server(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    print(name,password)
    return render(request, 'student/studlogin.html')



# get and post method for studregister_using_django_forms.html
from student.forms import studRegister
def registration(request):
    form=studRegister()
    context={}
    context['form']=form
    if request.method=="POST":
        form=studRegister(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            print(name)
            return render(request, 'student/studregister_using_django_forms.html', context)


    return render(request,'student/studregister_using_django_forms.html',context)

























