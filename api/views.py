from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .models import Student

# Create your views here.
class ValidStudent(APIView):
    def post(self,request):
        name = request.data.get('name')
        # print(name)
        # name_validate = Student.objects.get(name=name)
        # email = name_validate.email
        # validation = Student.objects.get(name=name)
        # if  validation==True:
        #     # name_validate = Student.objects.only('id').get(name=name).id
        #     print("It is there")
        #     # print(name_validate.email)
        #     return Response(status=status.HTTP_200_OK)
        # else:
        #     print("Not there")
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            validation = Student.objects.get(name=name)
            print(validation)
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            print('not')
            return Response(status=status.HTTP_404_NOT_FOUND)
