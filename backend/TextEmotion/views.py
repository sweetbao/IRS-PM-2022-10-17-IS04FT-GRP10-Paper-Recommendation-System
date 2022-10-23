from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Paper
from .serializers import PaperSerializer



class PaperViewSet(viewsets.ModelViewSet):

     queryset = Paper.objects.all().order_by('-retrievetime')
     serializer_class = PaperSerializer
     def get_queryset(self):
        title = self.request.query_params.get("title", None)
        if title:
            qs = Paper.objects.filter()
            qs = qs.filter(title=title)

            return qs

        return super().get_queryset()

