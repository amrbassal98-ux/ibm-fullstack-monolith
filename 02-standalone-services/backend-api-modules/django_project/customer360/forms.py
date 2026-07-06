from django import forms
from .models import Customer, Interaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AgentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'corporate.email@company.com'}))
    first_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply standard Bootstrap classes across legacy fields inherited from the base class
        for field_name in self.fields:
            if field_name != 'email' and field_name != 'first_name' and field_name != 'last_name':
                self.fields[field_name].widget.attrs['class'] = 'form-control'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'social_media']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@domain.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address'}),
            'social_media': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://socialprofile.com'}),
        }


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['channel', 'direction', 'summary']
        widgets = {
            'channel': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'direction': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Provide a summary of the interaction...'}),
        }