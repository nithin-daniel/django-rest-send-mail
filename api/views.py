from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student

# Create your views here.
class ValidStudent(APIView):
    def post(self,request):
        name = request.data.get('name')
        # print(name)
        name_validate = Student.objects.filter(name=name)
        if name_validate.exists():
            print("It is there")
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
