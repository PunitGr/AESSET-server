from rest_framework import serializers

from .models import (Student, Subject,
                     Room, Faculty, DateSheet)


"""
Serializers renders the model instances into the JSON format
Example:
JSON objects may look like this:
{
    "status": "success",
    "data": {
        "query": "Exam"
    }
}
"""


# Serializes the Student Model instances into JSON format
class StudentSerializer(serializers.ModelSerializer):
    """
    Handles Student
    """
    class Meta:
        model = Student
        fields = ('__all__')


class StudentEnrolledSerializer(serializers.ModelSerializer):
    """
    Serializes the Student model instances except these fields:
    subject, semester, name.
    """
    class Meta:
        model = Student
        exclude = ['subject', 'semester', 'name']


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializes the Subject model instances into JSON format
    It also includes Students enrolled in a particular subject
    """
    students = StudentEnrolledSerializer(many=True, read_only=True,
                                         source='student_set')

    class Meta:
        model = Subject
        fields = ('subject_id', 'subject_name',
                  'department', 'paper_code', 'students')


class ExamDateSerializer(serializers.ModelSerializer):
    """
    Serializes the Datesheet model instance.
    """
    class Meta:
        model = DateSheet
        exclude = ['subject_id']


class StudentExamSerializer(serializers.ModelSerializer):
    # For datesheet list
    class Meta:
        model = Student
        fields = ('roll_no',)


class DateSheetSerializer(serializers.ModelSerializer):
    # List all the students of a particualar subject
    # having an exam of particualar subject
    students = StudentExamSerializer(many=True, read_only=True,
                                     source='student_set')
    exam = ExamDateSerializer(many=True, read_only=True,
                              source='datesheet_set')

    class Meta:
        model = Subject
        fields = ('subject_id', 'students', 'exam')


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializes the Room model instances.
    """
    class Meta:
        model = Room
        fields = ('__all__')


class FacultySerializer(serializers.ModelSerializer):
    """
    Serializes the Faculty model instances.
    """
    class Meta:
        model = Faculty
        fields = ('__all__')
