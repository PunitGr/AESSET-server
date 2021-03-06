from django.contrib import admin
from .models import QueryToken

"""
Django Admin reads metadata from the models to provide a quick,
model-centric interface where trusted users can manage content on the site.
The admin’s recommended use is limited to an organization’s
internal management tool. It’s not intended for building the
entire front end around.
"""


# Query Admin for displaying Query table in Django Admin
class QueryAdmin(admin.ModelAdmin):
    list_display = ('student', 'query_type', 'email',
                    'phone', 'token_id')
    list_filter = ('query_type', 'department', 'status')
    search_fields = ('query_type', 'student', 'email',
                     'phone', 'token_id')
    ordering = ('token_id',)


admin.site.register(QueryToken, QueryAdmin)
