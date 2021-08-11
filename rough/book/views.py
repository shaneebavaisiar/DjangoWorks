from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
# @csrf_exempt
class BookList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self,request,*args,**kwargs):
        return self.list( request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        return self.create( request, *args, **kwargs)

class BookDetails(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def put(self,request,*args,**kwargs):
        return self.update( request, *args, **kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve( request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy( request, *args, **kwargs)

