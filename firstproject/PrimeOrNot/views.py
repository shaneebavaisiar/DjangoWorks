from django.shortcuts import render

# Create your views here.

def prime(request):
    return render(request,'PrimeOrNot/prime.html')

def checkprime(request):
    number=request.POST.get('number')
    num=int(number)
    flag = 0
    if(num==1):
        print(num,'is not prime')
    else:
        for i in range(2, num):
            if (num % i == 0):
                flag += 1
                break
            else:
                flag = 0

        if (flag == 1):
            print(num,'is not prime')
        else:
            print(num,'is prime')

    return render(request,'PrimeOrNot/prime.html')

def prime1(request):
    return render(request,'PrimeOrNot/prime1.html')

def PrimeNbrs(request):
    first=request.POST.get('first')
    first=int(first)
    second=request.POST.get('second')
    second=int(second)
    flag=0
    for i in range(first,second+1):
        for j in range(2,i):
            if(i%j==0):
                flag+=1
                break
            else:
                flag=0
        if(flag==0):
            print(i)
    return render(request,'PrimeOrNot/prime1.html')
