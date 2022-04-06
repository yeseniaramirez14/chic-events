from django import forms
from django.http import HttpResponseRedirect 
from django.shortcuts import render     
from events.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


# class ContactForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="First Name")
#     last_name = forms.CharField(max_length=100, label="Last Name")
#     email = forms.EmailField(label="Your email address*", error_messages={'required': 'Please enter your email'})
#     comment = forms.CharField(widget=forms.Textarea, label="Write a message")

# def contact(request):
#     submitted = False
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # assert False
#             return HttpResponseRedirect('/message_sent')
#     else: 
#         form = ContactForm()
#         if 'submitted' in request.GET:
#             submitted = True
    
#     return render(request, 'events/contact.html', {'form': form, 'submitted': submitted})
