from django import forms
from . models import item,purchase,sale
class add_item_form(forms.ModelForm):
    class Meta:
        model=item
        exclude = ['name']
        fields='__all__'
class purchase_form(forms.ModelForm):
    class Meta:
        model=purchase
        exclude = ['name','total']
        fields='__all__'
