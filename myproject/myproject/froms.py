from django import forms 

class RegisterFrom(forms.Form):
    nombre =  forms.CharField (required=True,
                              max_length=244)
    email = forms.EmailField(required=True,
                             max_length=244)
    passw = forms.CharField(required=True,max_length=256,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-controlform-control'
                                }))