from django.core.mail import send_mail

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from seating_manager.models import Student
from .models import QueryToken
from .serializers import QuerySerializer

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


class UpdateQueryView(APIView):
    def get_object(self, token_id):
        try:
            token = QueryToken.objects.get(token_id=token_id)
        except QueryToken.DoesNotExist:
            return Response(
                {
                    "status": "failed",
                    "error": "Token not found",
                    "results": ""
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return token

    def patch(self, request, token_id):
        data = request.data
        query = self.get_object(token_id)
        serializer = QuerySerializer(query, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': 'success',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "failed",
                "error": serializer.errors,
                "results": ""
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class RequestQuery(APIView):
    def post(self, request):
        """
        Handles the POST request which helps a user to send a
        query to the server which first checks that if the student is
        exists in the Database. If the student exists it provides him with the
        timeslot and a token for query handling.
        """
        if request.method == 'POST':
            serializer = QuerySerializer(data=request.data)
            if serializer.is_valid():
                if Student.objects.get(system_id=serializer.validated_data['student']):
                    obj = Student.objects.get(
                        system_id=serializer.validated_data['student']
                    )
                    serializer.validated_data['department'] = obj.branch
                    serializer.validated_data['year'] = obj.year
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


class QueryList(APIView):
    def get(self, request):
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
