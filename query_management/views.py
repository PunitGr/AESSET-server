from django.core.mail import send_mail

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from seating_manager.models import Student
from .models import QueryToken
from .serializers import QuerySerializer


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
        query_type = request.GET.get('query_type')
        department = request.GET.get('department')
        year = request.GET.get('year')

        if date and status:
            querytoken = QueryToken.objects.filter(status=status, date=date)
            serializer = QuerySerializer(querytoken, many=True)

        elif date and status and query_type:
            querytoken = QueryToken.objects.filter(status=status,
                                                   date=date,
                                                   query_type=query_type)
            serializer = QuerySerializer(querytoken, many=True)

        elif date and status and query_type and department:
            querytoken = QueryToken.objects.filter(status=status,
                                                   date=date,
                                                   query_type=query_type,
                                                   department=department)
            serializer = QuerySerializer(querytoken, many=True)

        elif date and status and query_type and department and year:
            querytoken = QueryToken.objects.filter(status=status,
                                                   date=date,
                                                   query_type=query_type,
                                                   department=department,
                                                   year=year)
            serializer = QuerySerializer(querytoken, many=True)

        elif date and status and department and year:
            querytoken = QueryToken.objects.filter(status=status,
                                                   date=date,
                                                   department=department,
                                                   year=year)
            serializer = QuerySerializer(querytoken, many=True)

        elif date and department and year:
            querytoken = QueryToken.objects.filter(status=status,
                                                   date=date,
                                                   department=department,
                                                   year=year)
            serializer = QuerySerializer(querytoken, many=True)

        elif date and status and department:
            querytoken = QueryToken.objects.filter(status=status,
                                                   date=date,
                                                   department=department,
                                                   )
            serializer = QuerySerializer(querytoken, many=True)

        elif date and department:
            querytoken = QueryToken.objects.filter(department=department)
            serializer = QuerySerializer(querytoken, many=True)

        else:
            querytoken = QueryToken.objects.filter(date=date)
            serializer = QuerySerializer(querytoken, many=True)

        return Response(serializer.data)
