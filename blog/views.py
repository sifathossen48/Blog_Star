from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import AboutInfo,NewsItem, Slider, Testimonial
from blog.serializers import AboutInfoSerializer, ContactFormSerializer, NewsItemSerializer, SliderSerializer, TestimonialSerializer

# Create your views here.
class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class NewsItemListView(generics.ListAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

class AboutInfoView(generics.ListAPIView):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoSerializer

class TestimonialView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ContactFormCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact form submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)