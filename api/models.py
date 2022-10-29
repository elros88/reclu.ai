from django.db import models

# Create your models here.

class Interview(models.Model):
  candidate_name = models.CharField(max_length=255, blank=False, unique=True)
  interview = models.TextField()
  position = models.CharField(max_length=500, blank=False)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)


class Summary(models.Model):
  summary = models.TextField()
  interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
  prompt = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)


class ToolsExtraction(models.Model):
  tools = models.TextField()
  interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
  prompt = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)