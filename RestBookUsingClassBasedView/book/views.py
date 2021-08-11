from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse
from django.http import JsonResponse

class BookList(APIView):
    def get(self,request):
        lst_book=list(Book.objects.values("book_name","author","price").order_by('id'))
        print(lst_book)
        return Response(lst_book)
        # books=Book.objects.all().values()
        # print(Book.objects.all())
        # print(books)
        # obj=[]
        # for i in books:
        #     obj.append(i)
        # print(obj)
        # # serializer=BookSerializer(books,many=True)
        # return JsonResponse(obj,safe=False)


    def post(self,request):

        serializer=BookSerializer(data=request.data)
        print(request.data)
        data=request.data
        print(data['book_name'])
        book_name=data['book_name']
        author=data['author']
        price=data['price']
        Book.objects.create(book_name=book_name,author=author,price=price)
        return Response('sucess')


class BookDetail(APIView):
    def get_object(self,id):
        return Book.objects.get(id=id)
    def get(self,request,id):
        book=self.get_object(id)
        return JsonResponse({"id":book.id,"book_name":book.book_name,"author":book.author,"price":book.price})
    def put(self,request,id):
        book=self.get_object(id)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        book=self.get_object(id)
        book.delete()
        return Response('deleted',status=status.HTTP_204_NO_CONTENT)