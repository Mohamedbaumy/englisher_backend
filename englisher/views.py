from django.shortcuts import render
from .models import Pricing, FreeVideo, Testimonials, Sponsor, FoundrFeature, Team, EnglisherFeature
from django.contrib.auth.decorators import login_required
from .forms import EmailForm
from django.core.mail import send_mail
from django.http import JsonResponse


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


def add_email(request):
    data = {'success': False}
    if request.method=='POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            data['success'] = True
        # send_mail("New Mail", "lol", "mahmoud.elneshawy@english-er.com",
        #          ["nn0114250@gmail.com", ])
    data['message'] = "Thank you for Subscribe!"
    return JsonResponse(data)
