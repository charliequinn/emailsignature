from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import EmailSignatureForm


class GenerateSignatureView(FormView):
    template_name = 'index.html'
    form_class = EmailSignatureForm
    success_url = reverse_lazy('email_signature_ready')

    def form_valid(self, form):
        self.request.session.update(form.cleaned_data)
        return super(GenerateSignatureView, self).form_valid(form)


class GenerateSignatureABView(GenerateSignatureView):
    template_name = 'index_ab.html'
    success_url = reverse_lazy('email_signature_ab_ready')


class GenerateSignatureRBView(GenerateSignatureView):
    template_name = 'index_rb.html'
    success_url = reverse_lazy('email_signature_rb_ready')


class DisplayEmailSignatureView(TemplateView):
    template_name = 'email_signature.html'


class DisplayABEmailSignatureView(TemplateView):
    template_name = 'email_signature_ab.html'


class DisplayRBEmailSignatureView(TemplateView):
    template_name = 'email_signature_rb.html'
