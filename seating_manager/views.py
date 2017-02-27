# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Subject, Room, Faculty
from .serializers import (StudentSerializer, RoomSerializer,
                          FacultySerializer, SubjectSerializer,
                          DateSheetSerializer)


# CRUD - Student View
class StudentListView(APIView):
    # List details of all students
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    # Create a Student object
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    # Delete a Student object
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD - Subject view
class SubjectListView(APIView):
    # List details of all subjects
    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

    # Create Subject object
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Subject object
    def delete(self, request, pk):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD - Room List view
class RoomListView(APIView):
    # List details of all rooms
    def get(self, request):
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    # Create Room list object
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Room list object
    def delete(self, request, pk):
        room = self.get_object(pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD - Faculty list view
class FacultyListView(APIView):
    # List details of all faculties
    def get(self, request):
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(serializer.data)

    # Create Faculty list object
    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Faculty list object
    def delete(self, request, pk):
        faculty = self.get_object(pk)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD - Datesheet view
class DateSheetView(APIView):
    # List details of all faculties
    def get(self, request):
        dateSheet = Subject.objects.all()
        serializer = DateSheetSerializer(dateSheet, many=True)
        return Response(serializer.data)

    # Create Datesheet view
    def post(self, request):
        serializer = DateSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Datesheet view
    def delete(self, request, pk):
        dateSheet = self.get_object(pk)
        dateSheet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
