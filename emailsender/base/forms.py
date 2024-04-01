from django import forms

class SignUp(forms.Form):
    username = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    email = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))