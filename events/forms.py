from django import forms
from events.models import BookRequest, Contact, Event
forms.DateInput.input_type="date"
forms.TimeInput.input_type="time"



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class BookRequestForm(forms.ModelForm):
    package = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), widget=forms.RadioSelect)
    class Meta:
        model = BookRequest
        fields = "__all__"

        