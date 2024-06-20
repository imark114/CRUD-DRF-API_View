from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer
# Create your views here.

class TeacherApiView(APIView):
    def get(self,request, pk=None):
        if pk is not None:
            tch = Teacher.objects.get(id=pk)
            serializer = TeacherSerializer(tch)
            return Response(serializer.data)
        tch = Teacher.objects.all()
        serializer = TeacherSerializer(tch, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Inserted Successfully!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk):
        tch = Teacher.objects.get(id=pk)
        serializer = TeacherSerializer(tch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Updated Successfull!!'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request, pk):
        tch = Teacher.objects.get(id=pk)
        serializer = TeacherSerializer(tch,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Updated Successfull!!'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tch = Teacher.objects.get(id=pk)
        tch.delete()
        return Response({'msg':'Delted Successfully'}, status= status.HTTP_200_OK)