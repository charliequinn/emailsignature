from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import GenerateSignatureView, DisplayEmailSignatureView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', GenerateSignatureView.as_view(), name="detail"),
    url(r'^email-signature/', DisplayEmailSignatureView.as_view(), name="email_signature_ready"),
    url(r'^admin/', include(admin.site.urls)),
)
