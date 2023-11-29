from dataclasses import field
from django import forms
from base.models import Car, Payments


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'
        # fields = ['name','email_address','phone_number','address','town_city','pickup_location','pickup_date','dropoff_location','dropoff_date','payment_ref','payment_amount']


class AddCarForm(forms.ModelForm):
    car_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    car_type = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'SUV or Sport or Van'}))
    brief_description_of_the_car = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'what does your car have that makes it cool'}))
    car_category = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Manual or Automatic'}))
    no_of_seats = forms.IntegerField( widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of Seats'}))
    amount_per_day = forms.IntegerField( widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Amount Per Day'}))

    

    class Meta:
        model = Car
        fields = ['car_name','car_type','car_image','car_category','no_of_seats','amount_per_day']