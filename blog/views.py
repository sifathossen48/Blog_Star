from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
# from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from blog.filters import NewsItemFilter
from blog.models import AboutInfo,NewsItem, Slider, Testimonial
from blog.serializers import AboutInfoSerializer, ContactFormSerializer, NewsItemSerializer, SliderSerializer, TestimonialSerializer

# Create your views here.
class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class NewsItemListView(generics.ListAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsItemFilter
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset:
            return Response(
                {"detail": "No news items found for the given search criteria."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Otherwise, return the paginated or full list of results
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If no pagination is used, return the entire queryset data
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# class NewsItemSearchView(generics.ListAPIView):
#     queryset = NewsItem.objects.all()
#     serializer_class = NewsItemSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['title', 'content'] 

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