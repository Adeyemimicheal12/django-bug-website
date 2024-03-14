from django import forms

class BlogForms(forms.form):




   name=forms.CharField(max_length=200, required=True)