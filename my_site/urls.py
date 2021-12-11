"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
        name='logout'),
    path('password/change/',
        auth_views.PasswordChangeView.as_view(),
        name='change-password'),
        # success_url=reverse_lazy('category-list')
    path('', include("englisher.urls")),
    path('dashboard/', include("englisher.dashbord.pricing.urls")),
    path('dashboard/', include("englisher.dashbord.freevideo.urls")),
    path('dashboard/', include("englisher.dashbord.testimonials.urls")),
    path('dashboard/', include("englisher.dashbord.sponsor.urls")),
    path('dashboard/', include("englisher.dashbord.foundrfeature.urls")),
    path('dashboard/', include("englisher.dashbord.team.urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)