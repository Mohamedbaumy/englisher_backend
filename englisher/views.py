from django.shortcuts import render
from .models import Pricing, FreeVideo, Testimonials, Sponsor, FoundrFeature, Team, EnglisherFeature
from django.contrib.auth.decorators import login_required

def home(request):
    prices = Pricing.objects.filter(active=True)[:3]
    videos = FreeVideo.objects.filter(active=True)[:8]
    testimonials = Testimonials.objects.filter(active=True)[:10]
    sponsors = Sponsor.objects.filter(active=True)[:10]
    trmplate_name = "eng_templates/home.html"

    context = {
        "prices": prices,
        "videos": videos,
        "testimonials": testimonials,
        "sponsors": sponsors
    }
    return render(request, trmplate_name, context)


def about_founder(request):
    features = FoundrFeature.objects.filter(active=True)[:3]
    trmplate_name = "eng_templates/about.html"

    context = {
        "features": features
    }
    return render(request, trmplate_name, context)


def about_englisher(request):
    features = EnglisherFeature.objects.filter(active=True)[:3]
    trmplate_name = "eng_templates/about_englisher.html"

    context = {
        "features": features
    }
    return render(request, trmplate_name, context)


def team(request):
    teams = Team.objects.filter(active=True)
    trmplate_name = "eng_templates/team.html"

    context = {
        "teams": teams
    }
    return render(request, trmplate_name, context)
    

@login_required
def dashboard(request):
    trmplate_name = "dashboard/base.html"
    return render(request, trmplate_name, {})