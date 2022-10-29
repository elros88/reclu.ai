from rest_framework import serializers
from .models import Interview, Summary, ToolsExtraction


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('id', 'candidate_name', 'interview', 'position'
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id', 'summary', 'interview', 'prompt',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ToolsExtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolsExtraction
        fields = ('id', 'tools', 'interview', 'prompt',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')