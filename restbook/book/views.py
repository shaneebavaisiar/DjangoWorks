from django.shortcuts import render

from .serializers import BookSerializer
from .models import Book
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def book_list(request):
    if request.method=='GET':
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def book_detail(request,id):
    if request.method=='GET':
        book=Book.objects.get(id=id)
        serializer=BookSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        book=Book.objects.get(id=id)
        serializer=BookSerializer(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
    elif request.method=='DELETE':
        book=Book.objects.get(id=id)
        data=book.delete()
        return HttpResponse('deleted')