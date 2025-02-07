from django.urls import path

from blog.views import AboutInfoView, ContactFormCreateView, NewsItemListView, SliderListView, TestimonialView


urlpatterns = [
    path('sliders/', SliderListView.as_view(), name='slider-list'),
    path('news/', NewsItemListView.as_view(), name='news-list'),
    path('about/', AboutInfoView.as_view(), name='about-info'),
    path('testimonials/', TestimonialView.as_view(), name='testimonial-list'),
    path('contact/', ContactFormCreateView.as_view(), name='contact-form')
]
