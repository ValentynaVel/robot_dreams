from django import forms

from purchase.models import Purchase


class PurchaseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = Purchase
        fields = '__all__'
