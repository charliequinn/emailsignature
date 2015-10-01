from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import GenerateSignatureView, DisplayEmailSignatureView, GenerateSignatureABView, GenerateSignatureRBView, DisplayEmailSignatureABView, DisplayEmailSignatureRBView

urlpatterns = patterns('',
    url(r'^$', GenerateSignatureView.as_view(), name="detail"),
    url(r'^ab/$', GenerateSignatureABView.as_view(), name="ab_detail"),
    url(r'^rb/$', GenerateSignatureRBView.as_view(), name="rb_detail"),
    url(r'^email-signature/', DisplayEmailSignatureView.as_view(), name="email_signature_ready"),
    url(r'^email-signature-ab/', DisplayEmailSignatureABView.as_view(), name="email_signature_ab_ready"),
    url(r'^email-signature-rb/', DisplayEmailSignatureRBView.as_view(), name="email_signature_rb_ready"),
    url(r'^admin/', include(admin.site.urls)),
)
