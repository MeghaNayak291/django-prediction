from django import forms
from .models import Prediction


class PredictionForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'id': 'imageInput'
        }),
        label='Upload Strawberry Leaf Image'
    )

    class Meta:
        model = Prediction
        fields = ['image']
