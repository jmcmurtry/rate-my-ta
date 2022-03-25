import email
from django import forms 

class SignupForm(forms.Form): 
    #name = forms.CharField(label = 'Your Name', max_length = 100)
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))

class SearchForm(forms.Form):
    searchQuery = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))

class NewReviewForm(forms.Form):
    courseCode = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea'}))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea'}))
    body = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea2', 'style': 'height: 100px'}))
    rating = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-select', 'id': 'floatingSelect'}))

class HiddenForm(forms.Form):
    taId = forms.CharField(widget=forms.TextInput(attrs={'id': 'hiddenInput'}))