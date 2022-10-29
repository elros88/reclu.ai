from django.urls import path, include, re_path
from rest_framework import routers
from .views import InterviewListView, InterviewDetailView, SummaryListView, SummaryDetailView, ToolsExtractionListView, ToolsExtractionDetailView

router = routers.DefaultRouter()


urlpatterns = [
  re_path(r'^interview/', InterviewListView.as_view()),
  re_path(r'^interview-admin/', InterviewDetailView.as_view()),
  re_path(r'^summary/', SummaryListView.as_view()),
  re_path(r'^summary/(?P<pk>\d+)/$', SummaryDetailView.as_view()),
  re_path(r'^tools/$', ToolsExtractionListView.as_view()),
  re_path(r'^tools/(?P<pk>\d+)/$', ToolsExtractionDetailView.as_view()),
  path('', include(router.urls))
]