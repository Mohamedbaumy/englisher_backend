from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration, Pricing, FreeVideo, Testimonials, Sponsor, FoundrFeature, AboutFounder, Team


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(AboutFounder, SingletonModelAdmin)
admin.site.register(Pricing)
admin.site.register(FreeVideo)
admin.site.register(Testimonials)
admin.site.register(Sponsor)
admin.site.register(FoundrFeature)
admin.site.register(Team)
