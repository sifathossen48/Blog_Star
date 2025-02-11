from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from blog.views import AboutInfoView, ContactFormCreateView, LoginView, LogoutView, NewsItemDetailView, NewsItemListView, RegisterView, SliderListView, TestimonialView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sliders/', SliderListView.as_view(), name='slider-list'),
    path('news/', NewsItemListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', NewsItemDetailView.as_view(), name='news-details'),
    # path('news/search/', NewsItemSearchView.as_view(), name='blog-search'),
    path('about/', AboutInfoView.as_view(), name='about-info'),
    path('testimonials/', TestimonialView.as_view(), name='testimonial-list'),
    path('contact/', ContactFormCreateView.as_view(), name='contact-form'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
