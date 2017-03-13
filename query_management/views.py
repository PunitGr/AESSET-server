from django.core.mail import send_mail
from django.db.models import F
from django.utils.text import slugify

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from seating_manager.models import Student
from .models import TimeSlot, QueryToken
from .serializers import QuerySerializer, TimeSlotSerializer

timeslot = {
    'A1': '9:30-10:00',
    'B1': '10:01-10:30',
    'C1': '10:31-11:00',
    'D1': '11:01-11:30',
    'F1': '11:31-12:00',
    'G1': '12:01-12:30',
    'H1': '1:30-2:00',
    'I1': '2:00-2:30'
}


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
                serializer.validated_data['slot'] = CreateSlot(
                    serializer.validated_data['date'],
                    serializer.validated_data['time']
                )
                query_obj = serializer.save()
                SendEmail(query_obj.email)
                return Response(
                    {
                        'status': 'success',
                        'data': serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
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


def CreateSlot(date, time):
    slug = slugify(time) + "-" + slugify(date)
    if TimeSlot.objects.filter(slot_id=slug).exists():
        slot = TimeSlot.objects.get(slot_id=slug)
        slot.count = F('count') + 1
        slot.save()
        return slot
    else:
        serializer = TimeSlotSerializer(data={"slot_id": slug, "count": 1})
        if serializer.is_valid():
            obj = serializer.save()
            return obj


@api_view(['GET'])
def QueryList(request):
    status = request.GET.get('status')
    date = request.GET.get('date')
    if date and status:
        querytoken = QueryToken.objects.filter(status=status, date=date)
        serializer = QuerySerializer(querytoken, many=True)
    elif status:
        querytoken = QueryToken.objects.filter(status=status)
        serializer = QuerySerializer(querytoken, many=True)
    elif date:
        querytoken = QueryToken.objects.filter(date=date)
        serializer = QuerySerializer(querytoken, many=True)
    else:
        querytoken = QueryToken.objects.all()
        serializer = QuerySerializer(querytoken, many=True)
    return Response(serializer.data)
