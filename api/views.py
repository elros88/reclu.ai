from django.shortcuts import render
from rest_framework import generics, viewsets, status, serializers, permissions, filters

from .serializers import  InterviewSerializer, SummarySerializer, ToolsExtractionSerializer
from .models import Interview, Summary, ToolsExtraction
# Create your views here.


class InterviewListView(generics.ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    name = 'interview-list'


class InterviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    name = 'interview-detail'


class SummaryListView(generics.ListCreateAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    name = 'summary-list'


class SummaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    name = 'summary-detail'


class ToolsExtractionListView(generics.ListCreateAPIView):
    queryset = ToolsExtraction.objects.all()
    serializer_class = ToolsExtractionSerializer
    name = 'tool-list'


class ToolsExtractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToolsExtraction.objects.all()
    serializer_class = ToolsExtractionSerializer
    name = 'tool-detail'