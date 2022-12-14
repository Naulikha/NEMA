from django import forms

from .models import Contacts, Comments


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'