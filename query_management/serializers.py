from rest_framework import serializers

from .models import Query, TimeSlot, Token

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
        model = Query
        fields = ('__all__')


# Serializes the TimeSlot Model instances into JSON format
class TimeSlotSerializer(serializers.ModelSerializer):
    """
    Handles Time slot
    """
    class Meta:
        model = TimeSlot
        fields = ('__all__')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('__all__')
