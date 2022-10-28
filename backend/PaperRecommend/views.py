import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from .dataStoreService import storeData, summaryGet, randomKeywords, testId, getRecommand
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
    #randomKeywords('stat.ML')
    #testId()
   # a = Paper.objects.get(id =99)
   # print(a.area)
    data = [75192,75099]
    getRecommand(data)



    return HttpResponse('添加成功')


class TestPaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all().order_by('-retrievetime')
    serializer_class = PaperSerializer
    def create(self, request):
        ids = request.data
        intId = []
        for id in ids:
            id = int(id)
            intId.append(id)
        if ids:
                qs = getRecommand(intId)
                json_data = serializers.serialize('json', qs)
                return HttpResponse(json_data, content_type="application/json")
        return super().create()



    '''
    
    queryset = Paper.objects.all().order_by('-retrievetime')
    serializer_class = PaperSerializer

    def post_queryset(self):
        ids = self.request.POST.get()
        print(ids)
        print(self.request.POST)
        if not ids:
            qs = getRecommand(ids)
            print(qs)

            return qs

        return super().post_queryset()'''



#def recommendGet(request):









