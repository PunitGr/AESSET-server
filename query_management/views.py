from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from seating_manager.models import Student
from .models import QueryToken
from .serializers import QuerySerializer
from .tasks import RequestQueryTask


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
                    RequestQueryTask.delay(query_obj)
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


class QueryList(APIView):
    def get(self, request):
        kwargs = {}
        status = request.GET.get('status')
        date = request.GET.get('date')
        query_type = request.GET.get('query_type')
        department = request.GET.get('department')
        year = request.GET.get('year')

        if status is not None:
            kwargs['status'] = str(status)

        if date is not None:
            kwargs['date'] = str(date)

        if query_type is not None:
            kwargs['query_type'] = str(query_type)

        if department is not None:
            kwargs['department'] = str(department)

        if year is not None:
            kwargs['year'] = str(year)

        querytoken = QueryToken.objects.filter(**kwargs)
        serializer = QuerySerializer(querytoken, many=True)

        return Response(serializer.data)
