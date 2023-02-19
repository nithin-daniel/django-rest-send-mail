from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from .models import Student

# Create your views here.
class ValidStudent(APIView):
    def post(self,request):
        name = request.data.get('name')
        try:
            validation = Student.objects.get(name=name)
            # print(validation.email) # It prints thw email
            recipient_list = [validation.email]
            subject = "Congratulations You are seleted "
            message = "This is a dummy data"
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
