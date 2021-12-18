from django.db import models
from solo.models import SingletonModel


COLOR_CHOICES = (
    ("success", "Green"),
    ("danger", "Red"),
    ("warning", "Yellow"),
)

class SiteConfiguration(SingletonModel):
    header_logo = models.ImageField(upload_to="images/logos/")
    footer_logo = models.ImageField(upload_to="images/logos/")
    footer_about = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    youtube_channel = models.URLField(blank=True, null=True)
    # Slider Configuration
    slider_image = models.ImageField(upload_to="images/slider/")
    slider_title = models.CharField(max_length=250)
    slider_body = models.CharField(max_length=1000, blank=True, null=True)
    #  Numers Configuration
    student_number = models.IntegerField(default=500)
    free_video_number = models.IntegerField(default=100)
    courses_number = models.IntegerField(default=20)
    hours_number = models.IntegerField(default=500)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


class Pricing(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    plan_included = models.TextField()
    payment_url = models.URLField()
    box_color = models.CharField(max_length=10,choices=COLOR_CHOICES)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FreeVideo(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/freevideo/")
    iframe = models.TextField()
    video_link = models.URLField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    author = models.CharField(max_length=250)
    author_image = models.ImageField(upload_to="images/testimonials/")
    what_he_say = models.TextField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250)
    sponsor_image = models.ImageField(upload_to="images/sponsors/")
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sponsor_name


class AboutFounder(SingletonModel):
    founder_name = models.CharField(max_length=250)
    founder_image = models.ImageField(upload_to="images/founder/")
    body = models.TextField()

    def __str__(self):
        return "About Founder"

    class Meta:
        verbose_name = "About Founder"


class FoundrFeature(models.Model):
    icon = models.CharField(max_length=100)
    value = models.CharField(max_length=250)
    body = models.TextField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


class Team(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/team/")
    jop = models.CharField(max_length=250, blank=True, null=True)
    about = models.TextField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

