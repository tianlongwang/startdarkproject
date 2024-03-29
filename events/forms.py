from django import forms
from events.models import Event


class EventForm(forms.ModelForm):
    description = forms.CharField(max_length=255, widget=forms.Textarea)
    
    class Meta:
        model = Event
        fields = ('description',)