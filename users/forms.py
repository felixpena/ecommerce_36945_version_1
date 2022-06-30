"""
from django import forms
from users.models import User_profile

# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField(required=False)


class Product_form(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = '__all__'
"""