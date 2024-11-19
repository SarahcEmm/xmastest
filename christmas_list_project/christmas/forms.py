from django import forms
from .models import ChristmasList, GiftItem

class ChristmasListForm(forms.ModelForm):
    class Meta:
        model = ChristmasList
        fields = ['title', 'description', 'visibility']

class GiftItemForm(forms.ModelForm):
    class Meta:
        model = GiftItem
        fields = ['name', 'description', 'link', 'purchased']
