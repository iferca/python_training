from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Your name', min_length=2)
    title = forms.CharField(label="Title", help_text="Mx will be used if not provided", required=False)
