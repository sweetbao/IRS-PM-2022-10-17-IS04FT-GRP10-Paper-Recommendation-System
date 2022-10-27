import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .dataStoreService import storeData, summaryGet,  randomKeywords
from .models import Paper
from .serializers import PaperSerializer



class PaperViewSet(viewsets.ModelViewSet):

     queryset = Paper.objects.all().order_by('-retrievetime')
     serializer_class = PaperSerializer
     def get_queryset(self):
        domain = self.request.query_params.get("domain", None)
        if domain:
            qs = randomKeywords(domain)

            return qs

        return super().get_queryset()


def addData(request):

    #storeData()
    #summaryGet()
    #keywordsGet()
    randomKeywords('stat.ML')


    return HttpResponse('添加成功')

