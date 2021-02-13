from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):
    name= forms.CharField(max_length=100)
    tel = forms.IntegerField()
    msg= forms.CharField(max_length=300)
