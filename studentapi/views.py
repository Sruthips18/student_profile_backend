from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import serializers
from studentapi.serializers import StudentSerializer,UserSerializer
from studentapi.models import Student

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class StudentProfileView(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()