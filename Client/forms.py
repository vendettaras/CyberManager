from ast import Pass
from dataclasses import fields
from msilib.schema import Error
from django import forms
from Client.models import Client, Operation

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'nom',
            'prenom',
            'email',
            'telephone',
            'addresse',
            'profession',
            'num_CIN',
            'sexe'
        ]

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'

class AbonnementForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'

