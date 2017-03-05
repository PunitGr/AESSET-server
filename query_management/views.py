import datetime
from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from seating_manager.models import Student
from .models import TimeSlot, Token, Query
from .serializers import QuerySerializer, TokenSerializer

string = "SU17"


def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped


@api_view(['POST'])
def RequestQuery(request):
    """
    Handles the POST request which helps a user to send a
    query to the server which first checks that if the student is
    exists in the Database. If the student exists it provides him with the
    timeslot and a token for query handling.
    """
    if request.method == 'POST':
        serializer = QuerySerializer(data=request.data)
        exists = False
        if serializer.is_valid():
            try:
                if Student.objects.get(system_id=serializer.validated_data['student']):
                    exists = True
            except Student.DoesNotExist:
                pass
            if exists:
                query_obj = serializer.save()
                GenerateTimeSlotToken(query_obj.student, query_obj.email)
                return HttpResponse("Email has been sent")
            else:
                response_data = 'User with this email id does not exist'
                return Response(
                    {
                        'status': 'failed',
                        'data': response_data
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors)


# Function to send an email to the specified email id
# To test please run the smtp server
# python -m smtpd -n -c DebuggingServer localhost:1025
def SendEmail(email):
    message = ("Hello there")
    send_mail("hello", message, "hey@sharda.ac.in", [email])


# class RequestQueryView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'

#     def post(self, request):
#         serializer = QuerySerializer(data=request.data)
#         if serializer.is_valid():
#             query_obj = serializer.save()


# Function to create a time slot
def UpdateTimeSlotValue():
    now = datetime.datetime.now()
    if (now.hour > 13 and now.minute > 45):
        # Date
        dd = now.date + 1
        # Year
        yy = now.year
        # Month
        mm = now.month
        date = datetime.date(yy, mm, dd)
        TimeSlot.objects.all().update(date=date, count=0)


# Function to generate a token
@counted
def GenerateTimeSlotToken(id, email):
    # now = datetime.datetime.now()
    # hour = now.hour
    # minute = now.minute
    # time = datetime.time(hour, minute)
    slot = TimeSlot.objects.filter(count__lt=5)

    if slot.exists():
        slot = slot[0]
        print (slot, id)
        token_no = GenerateTimeSlotToken.calls
        token = string + str(token_no)
        serializer = TokenSerializer(data={"slot": slot, "student_id": id, "token_id": token})
        print(serializer)
        if serializer.is_valid():
            print("valid")
            serializer.save()
            SendEmail(email)
        else:
            print(serializer.errors)
