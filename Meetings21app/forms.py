from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import * 
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

class HomePageBannerForm(forms.ModelForm):
    class Meta:
        model = HomePageBanner
        fields = ['home_page_banner_image', 'home_page_banner_text', 'home_page_banner_date']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = HomePageSubscribeForm
        fields = ['name','email']
        
class TicketsPriceForm(forms.ModelForm):
    class Meta:
        model = HomePageTicketsPrice
        fields = ['price']
