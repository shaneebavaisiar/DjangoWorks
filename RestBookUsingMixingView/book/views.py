from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer,LoginSerializer
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class BookList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # basic authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # {"token":"257423abc527b8f79ff654c6ca4dc5d37f190bfd"}
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class LoginApi(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get('username')
            password=serializer.validated_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_201_CREATED)
        return Response({"message":'login failed'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutApi(APIView):
    def get(self,request):
        logout(request)
        request.user.auth_token.delete()