from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, RedirectView

from .views import process_donation

urlpatterns = patterns(__package__ + '.views',
	url(r'^$', TemplateView.as_view(template_name='main/homepage.html'), name='home'),
	url(r'^kolibri/$', TemplateView.as_view(template_name='main/kolibri.html'), name='kolibri'),
    url(r'^map/$', RedirectView.as_view(url=reverse_lazy('map'))),
    url(r'^give/$', RedirectView.as_view(url=reverse_lazy('donate')), name='give'),
    url(r'^donate/$', TemplateView.as_view(template_name='main/donate.html'), {"STRIPE_PUBLISHABLE_API_KEY": settings.STRIPE_PUBLISHABLE_API_KEY}, name='donate'),
    url(r'^donate/process/$', process_donation, name='process_donation'),
    url(r'^directions/$', TemplateView.as_view(template_name='main/directions.html'), name='directions'),
)
