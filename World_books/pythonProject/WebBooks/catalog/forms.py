from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book

class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']

class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Muallif ismi")
    last_name = forms.CharField(label="Muallif familiyasi")
    date_of_birth = forms.DateField(label="Tug`ilgan sana",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type':'date'}))
    date_of_death = forms.DateField(label="O`lim sanasi",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type':'date'}))