from django import forms
from .models import Reservation


class ReservationForms(forms.ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class ': "form-control",
                                                                       'type': "text",
                                                                       "id ": "name",
                                                                       "placeholder": "Your Name *",
                                                                       "required": "",
                                                                       'class': "form-text text-danger flex-grow-1 lead",

                                                                       }))
    phone = forms.CharField(label='phone', widget=forms.TextInput(attrs={'class ': "form-control",
                                                                         'type':"tel",
                                                                         'placeholder':"Your Phone *",
                                                                         'required':"",
                                                                         'class':"form-text text-danger lead",
                                                                         }))




    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={"class ": "form-control",
                                                                           "type": "email",
                                                                           "id": "email",
                                                                           'placeholder': "Your Email *",
                                                                           'required': "",
                                                                           "class": "form-text text-danger lead",
                                                                           }))
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'class ': "form-control",
                                                                            'id':"message",
                                                                            'placeholder':"Your Message *",
                                                                            'required':'',
                                                                            'class':"form-text text-danger lead" ,
                                                                            }))

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'message', 'email',)
