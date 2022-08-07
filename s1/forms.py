from django import forms

class UserForm(forms.Form):
    num1 = forms.CharField(label='value1', max_length=100,widget=forms.TextInput())
    num2 = forms.CharField(label='value2', max_length=100)
    