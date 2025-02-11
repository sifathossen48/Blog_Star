from django.shortcuts import render
from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.views import APIView
# from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from blog.filters import NewsItemFilter
from blog.models import AboutInfo,NewsItem, Slider, Testimonial
from blog.pagination import CustomPagination
from blog.serializers import AboutInfoSerializer, ContactFormSerializer, NewsItemDetailSerializer, NewsItemSerializer, SliderSerializer, TestimonialSerializer, UserRegisterSerializer

# Create your views here.
# User Registration View
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# User Login View
class LoginView(APIView):
    permission_classes = [AllowAny]  
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'access_token': access_token,
                'refresh_token': str(refresh)
            })
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can log out

    def post(self, request):
        try:
            # Blacklist the refresh token
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()  # This invalidates the token
            return Response({"message": "Successfully logged out!"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
class SliderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class NewsItemListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsItemFilter
    pagination_class = CustomPagination
    
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

class NewsItemDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemDetailSerializer
    lookup_field = 'slug'

# class NewsItemSearchView(generics.ListAPIView):
#     queryset = NewsItem.objects.all()
#     serializer_class = NewsItemSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['title', 'content'] 

class AboutInfoView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoSerializer

class TestimonialView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ContactFormCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact form submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)