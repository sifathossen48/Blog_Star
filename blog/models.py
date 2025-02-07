from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name