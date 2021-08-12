from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Works
from .serializer import WorkSerializer
from rest_framework import status

class WorksGetPost(APIView):
    def get(self,request):
        res_data=Works.objects.all()
        serilaizer=WorkSerializer(res_data,many=True)
        return Response(serilaizer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serilaizer=WorkSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkUpdateDelete(APIView):
    def get_instance(self, id):
        return Works.objects.get(id=id)
    def get(self,request,id):
        res_data=self.get_instance(id)
        serializer=WorkSerializer(res_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self,request,id):
        res_data=self.get_instance(id)
        serilaizer=WorkSerializer(res_data,data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        rst_data=self.get_instance(id)
        rst_data.delete()
        return Response("deleted")