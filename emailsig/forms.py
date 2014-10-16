from django import forms

class EmailSignatureForm(forms.Form):
    full_name = forms.CharField(label='Your name *', max_length=100, required=True)
    job_title = forms.CharField(label='Job title *', max_length=100, required=True)
    email = forms.EmailField(label='Email *', max_length=100, required=True)
    main_contact_number = forms.CharField(label='Office number *', max_length=100, required=True)
    additional_number = forms.CharField(label='Mobile number', max_length=100, required=False)
    skype = forms.CharField(label='Skype', max_length=100, required=False)
