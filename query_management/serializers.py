from rest_framework import serializers

from .models import QueryToken

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


# Serializes the Query Model instances into JSON format
class QuerySerializer(serializers.ModelSerializer):
    """
    Handles Query Model requests
    """
    class Meta:
        model = QueryToken
        fields = ('id', 'student', 'query_type', 'query_type_value', 'email',
                  'phone', 'department', 'year', 'date', 'time', 'status',
                  'token_id', 'description')
