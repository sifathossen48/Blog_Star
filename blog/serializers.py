from rest_framework import serializers
from .models import AboutInfo, ContactForm, NewsItem, Slider, Testimonial

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

class NewsItemSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()
    class Meta:
        model = NewsItem
        fields = ['title','short_description','image','slug']
    def get_short_description(self, obj):
        return obj.content[:100] + "..." if len(obj.content) > 100 else obj.content

class NewsItemDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ['title','content','image','slug']

class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']