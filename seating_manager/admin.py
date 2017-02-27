from django.contrib import admin
from .models import Student, Faculty, Room, Subject, DateSheet

"""
Django Admin reads metadata from the models to provide a quick,
model-centric interface where trusted users can manage content on the site.
The admin’s recommended use is limited to an organization’s
internal management tool. It’s not intended for building the
entire front end around.
"""


# Student Admin for displaying Student table in Django Admin
class StudentAdmin(admin.ModelAdmin):
    # list_display displays the fields for the student
    list_display = ('roll_no', 'system_id', 'name',
                    'branch', 'year', 'semester')
    # list_filter filters student data with respect to the data entry given
    list_filter = ('roll_no', 'system_id', 'name',
                   'branch', 'year', 'semester')
    # search_fields for searching student data with respect to given searchable fields
    search_fields = ('roll_no', 'system_id', 'name',
                     'branch', 'year', 'semester')
    # for ordering of students by their roll number
    ordering = ('-roll_no',)


# Faculty Admin for displaying Faculty table in Django Admin
class FacultyAdmin(admin.ModelAdmin):
    # list_display displays the fields for the faculty
    list_display = ('department', 'faculty_id',
                    'designation', 'name')
    # list_filter filters data with respect to the data entry given
    list_filter = ('department', 'faculty_id',
                   'designation', 'name')
    # search_fields for searching faculty data with respect to given searchable fields
    search_fields = ('department', 'faculty_id',
                     'designation', 'name')
    # for ordering of faculty with respect to department
    ordering = ('-department',)


# Subject Admin for displaying Subject table in Django Admin
class SubjectAdmin(admin.ModelAdmin):
    # list_display displays the the fields for subject
    list_display = ('department', 'subject_id',
                    'subject_name', 'paper_code')
    # list_filter filters the subjects with respect to data entry given
    list_filter = ('department', 'subject_id',
                   'subject_name', 'paper_code')
    # search_fields for searching subject data with espect to given searchable fields
    search_fields = ('department', 'subject_id',
                     'subject_name', 'paper_code')
    # ordering subject department wise
    ordering = ('-department',)


# Room Admin for displaying Room table in Django Admin
class RoomAdmin(admin.ModelAdmin):
    #  list_display for displaying the fields for  the room
    list_display = ('room_number', 'room_type',
                    'capacity', 'block_number',
                    'building_name')
    # list_filter filters the room with respect to data enty given
    list_filter = ('room_number', 'room_type',
                   'capacity', 'block_number',
                   'building_name')
    #  for searching room data with respect to given searchable fields
    search_fields = ('room_number', 'room_type',
                     'capacity', 'block_number')
    #  for ordering rooms with respect to room numbers
    ordering = ('-room_number',)


#  Datesheet Admin for displaying Datesheet table in Django Admin
class DateSheetAdmin(admin.ModelAdmin):
    # list_display for displaying the exam date
    list_display = ('exam_date',)
    # filters with respect to the data entry given
    list_filter = ('subject_id', 'exam_date')
    # searches with respect to the entered data
    search_fields = ('subject_id', 'exam_date')
    # orders datesheet with respect to exam date
    ordering = ('exam_date',)


#  Change the admin site name AESSET
admin.site.site_header = "AESSET"
admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(DateSheet, DateSheetAdmin)
