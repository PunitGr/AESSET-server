from __future__ import unicode_literals

from django.db import models


# Create Stubject table
class Subject(models.Model):
    subject_id = models.CharField(blank=False, primary_key=True,
                                  max_length=12, default=None)
    subject_name = models.CharField(blank=False, max_length=48,
                                    default=None)
    department = models.CharField(max_length=12, default='CSE')
    paper_code = models.CharField(unique=True, max_length=12,
                                  default=None)

    def __str__(self):
        return self.subject_id


# Create Student table
class Student(models.Model):
    roll_no = models.IntegerField(blank=False, primary_key=True)
    system_id = models.IntegerField(blank=False, unique=True)
    name = models.CharField(blank=False, max_length=48)
    branch = models.CharField(blank=False, max_length=48)
    year = models.CharField(max_length=2)
    semester = models.CharField(blank=False, max_length=2)
    subject = models.ManyToManyField(Subject, blank=False, default=None)

    def __str__(self):
        return str(self.roll_no)


# used as choice field for classes
Room_choices = (
    ('Audi', 'Auditorium'),
    ('Classroom', 'Classroom'),
)


# Create Room table
class Room(models.Model):
    room_number = models.IntegerField(blank=False, unique=True)
    room_type = models.CharField(max_length=20, choices=Room_choices,
                                 default='Classroom')
    capacity = models.IntegerField(blank=False, default=64)
    block_number = models.IntegerField(blank=False)
    building_name = models.CharField(blank=False, max_length=12)

    def __str__(self):
        return str(self.room_number)


# used as choice field for faculty
faculty_choices = (
    ('Assistant_Professor', 'Assistant Professor'),
    ('Professor', 'Professor'),
    ('Non-Teaching', 'Non-Teaching')
)


# Create Faculty model
class Faculty(models.Model):
    faculty_id = models.IntegerField(blank=False, unique=True)
    name = models.CharField(blank=False, max_length=48)
    department = models.CharField(blank=False, max_length=12)
    designation = models.CharField(max_length=20, choices=faculty_choices,
                                   default='Assistant_Professor')

    def __str__(self):
        return str(self.faculty_id)

    # For conversion into plural form
    class Meta:
        verbose_name_plural = "Faculties"


# Create Datesheet table
class DateSheet(models.Model):
    subject_id = models.ManyToManyField(Subject, blank=False,
                                        default=None)
    exam_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.subject_id)

    # For conversion into plural form
    class Meta:
        verbose_name_plural = "Datesheet"
