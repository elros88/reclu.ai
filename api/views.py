from django.shortcuts import render
from django.conf import settings

from rest_framework.response import Response
from rest_framework import generics, viewsets, status, serializers, permissions, filters

import cohere
import pandas as pd

from .serializers import  InterviewSerializer, SummarySerializer, ToolsExtractionSerializer
from .models import Interview, Summary, ToolsExtraction
from .prompts import SUMMARY_PROMPT, EXTRACTION_PROMPT
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

    def post(self, request, *args, **kwargs):
        interview_id = request.data.get("interview", "")
        interview = Interview.objects.get(id=interview_id)

        if not interview:
            return Response(
                data={"message": "Interview not found in the system"},
                status=status.HTTP_400_BAD_REQUEST
            )

        prompt = ("{} \n interview: {} \n1% Summary:".format(SUMMARY_PROMPT, interview.interview))
        co = cohere.Client(settings.SECRET_COHERE)

        prediction = co.generate(
            model='xlarge',
            prompt=prompt,
            max_tokens=200,
            temperature=0.7,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods='NONE'
        )

        if not prediction.generations[0].text:
            return Response(
                data={"message": "Error creating summary"},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = prediction.generations[0].text
        print(f"RESPONSE: " + response)

        summary = Summary(summary = response,
                          prompt = prompt,
                          interview = interview)

        summary.save()

        return Response(
            data={'message': 'SUMMARY CREATED SUCCESSFULLY \n\n {}'.format(response)},
            status=status.HTTP_200_OK)


class SummaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    name = 'summary-detail'


class ToolsExtractionListView(generics.ListCreateAPIView):
    queryset = ToolsExtraction.objects.all()
    serializer_class = ToolsExtractionSerializer
    name = 'tool-list'

    def post(self, request, *args, **kwargs):
        interview_id = request.data.get("interview", "")
        interview = Interview.objects.get(id=interview_id)

        if not interview:
            return Response(
                data={"message": "Interview not found in the system"},
                status=status.HTTP_400_BAD_REQUEST
            )

        prompt = ("{}{} \n The tools used by the candidate are:".format(EXTRACTION_PROMPT, interview.interview))
        co = cohere.Client(settings.SECRET_COHERE)

        print(f"Prompt: " + prompt)

        prediction = co.generate(
          model='large',
          prompt=prompt,
          max_tokens=150,
          temperature=0.1,
          stop_sequences=["--"]
        )

        if not prediction.generations[0].text:
            return Response(
                data={"message": "Error extracting tools"},
                status=status.HTTP_400_BAD_REQUEST
            )

        tools_extraction = ToolsExtraction(tools = prediction.generations[0].text,
                          prompt = prompt,
                          interview = interview)

        tools_extraction.save()

        return Response(
            data={'message': 'TOOLS EXTRACTED SUCCESSFULLY{}'.format(prediction.generations[0].text)},
            status=status.HTTP_200_OK)


class ToolsExtractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToolsExtraction.objects.all()
    serializer_class = ToolsExtractionSerializer
    name = 'tool-detail'