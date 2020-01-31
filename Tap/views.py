from django.shortcuts import render
from rest_framework import generics
from .models import City
from .serializers import CitySerializer, HotelSerializer
from . import WebScrapping
from textblob import TextBlob


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = HotelSerializer


def a(request):
    WebScrapping.data2database()
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)


def b(request):
    c = City.objects.all()[0]
    for i in c.hotels:
        a = 0
        q = 0
        try:
            for j in i["Reviews"]:
                t = TextBlob(j['Text'])
                a += t.sentiment.polarity
                q += 1
                print(q)
        except:
            continue
        a = a/q
        i['Blob'] = a
    c.save()
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)


def c(request):
    c = City.objects.all()[0]
    for i in c.hotels:
        try:
            if i['Blob'] < 0.29:
                i['Blob'] = 'NEGATIVE'
            elif i['Blob'] < 0.35:
                i['Blob'] = 'NEUTRAL'
            else:
                i['Blob'] = 'POSITIVE'
        except:
            continue
            #i['Blob'] == 'Neutral'
    c.save()
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)


def d(request):
    c = City.objects.all()[0]
    for i in c.hotels:
        try:
            i['Description'] = i['Description'][:80] + '...'
        except:
            continue  # i['Blob'] == 'Neutral'
    c.save()
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)
