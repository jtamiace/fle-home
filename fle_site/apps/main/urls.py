from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect

from .views import process_donation, file_upload, cc_indiegogo_signup

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', TemplateView.as_view(template_name='main/homepage.html'), name='home'),
    url(r'^kolibri/', lambda request: HttpResponseRedirect(reverse('indiegogo'))),
    url(r'^cc_indiegogo_signup/$', 'cc_indiegogo_signup', name='cc_indiegogo_signup'),
    url(r'^indiegogo/$', TemplateView.as_view(template_name='main/kickstarter.html'), name='indiegogo'),
    url(r'^map/$', RedirectView.as_view(url=reverse_lazy('map'))),
    url(r'^give/$', RedirectView.as_view(url=reverse_lazy('donate')), name='give'),
    url(r'^donate/$', TemplateView.as_view(template_name='main/donate.html'), {"STRIPE_PUBLISHABLE_API_KEY": settings.STRIPE_PUBLISHABLE_API_KEY}, name='donate'),
    url(r'^donate/process/$', process_donation, name='process_donation'),
    url(r'^directions/$', TemplateView.as_view(template_name='main/directions.html'), name='directions'),
    url(r'^mailchimp/$', TemplateView.as_view(template_name='main/partials/_kickstarter_mailchimp.html'), name='mailchimp'),
    url(r'^fileupload/$', file_upload, name='file_upload'),
)
