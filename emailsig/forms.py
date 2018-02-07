from django import forms

class EmailSignatureForm(forms.Form):
    full_name = forms.CharField(label='Full name *', max_length=40, required=True)
    job_title = forms.CharField(label='Job title *', max_length=40, required=True)
    main_contact_number = forms.CharField(label='Office number *', max_length=15, required=True)
    additional_number = forms.CharField(label='Mobile number', max_length=15, required=False)
    address_line_1 = forms.CharField(label='Address line 1 (Building, Street)', max_length=40, required=False)
    address_line_2 = forms.CharField(label='Address line 2 (City)', max_length=30, required=False)
    address_line_3 = forms.CharField(label='Address line 3 (Postcode)', max_length=15, required=False)
    website = forms.CharField(label='Website', max_length=70, required=False, initial="www.twigeducation.com")


