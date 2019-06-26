from django import forms

from .models import Message

class CreateMessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'message')
        widgets = {'sender': forms.HiddenInput}