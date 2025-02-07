from django.contrib import admin

from blog.models import AboutInfo, ContactForm, NewsItem, Slider, Testimonial

# Register your models here.
admin.site.register(Slider)
admin.site.register(NewsItem)
admin.site.register(AboutInfo)
admin.site.register(Testimonial)
admin.site.register(ContactForm)