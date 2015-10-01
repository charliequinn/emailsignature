from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import EmailSignatureForm


class GenerateSignatureView(FormView):
    template_name = 'index.html'
    form_class = EmailSignatureForm
    success_url = reverse_lazy('email_signature_ready')

    def form_valid(self, form):
        self.request.session['full_name'] = form.cleaned_data['full_name']
        self.request.session['job_title'] = form.cleaned_data['job_title']
        self.request.session['main_contact_number'] = form.cleaned_data['main_contact_number']
        self.request.session['additional_number'] = form.cleaned_data['additional_number']
        self.request.session['email'] = form.cleaned_data['email']
        self.request.session['skype'] = form.cleaned_data['skype']

        return super(GenerateSignatureView, self).form_valid(form)


class GenerateSignatureABView(GenerateSignatureView):
    success_url = reverse_lazy('email_signature_ab_ready')

    def form_valid(self, form):
        return super(GenerateSignatureABView, self).form_valid(form)


class GenerateSignatureRBView(GenerateSignatureView):
    success_url = reverse_lazy('email_signature_rb_ready')

    def form_valid(self, form):
        return super(GenerateSignatureABView, self).form_valid(form)


class DisplayEmailSignatureView(TemplateView):
    template_name = 'email_signature.html'


class DisplayABEmailSignatureView(TemplateView):
    template_name = 'email_signature_ab.html'


class DisplayRBEmailSignatureView(TemplateView):
    template_name = 'email_signature_rb.html'
