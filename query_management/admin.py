from django.contrib import admin
from .models import Query, Token, TimeSlot

"""
Django Admin reads metadata from the models to provide a quick,
model-centric interface where trusted users can manage content on the site.
The admin’s recommended use is limited to an organization’s
internal management tool. It’s not intended for building the
entire front end around.
"""


# Query Admin for displaying Query table in Django Admin
class QueryAdmin(admin.ModelAdmin):
    list_display = ('student', 'query_type',
                    'created_at', 'modified_at', 'email',
                    'phone')
    list_filter = ('query_type', 'student', 'email',
                   'phone')
    search_fields = ('query_type', 'student', 'email',
                     'phone')
    ordering = ('created_at',)


# Token Admin for displaying Token table in Django Admin
class TokenAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'token_id', 'slot_id')
    list_filter = ('student_id', 'token_id', 'slot_id')
    search_fields = ('token_id', 'student_id', 'slot_id')


# TimeSlot Admin for displaying Timeslot table in Django Admin
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'date', 'start', 'finish')
    list_filter = ('date', 'slot_id')
    search_fields = ('date', 'slot_id')


admin.site.register(Query, QueryAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
