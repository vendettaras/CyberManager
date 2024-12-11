from django.db import models
from django.urls import reverse
from datetime import datetime

class Client(models.Model) :
    SEXE = (
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    )

    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    telephone = models.CharField( max_length=25)
    addresse = models.CharField(max_length=25)
    profession = models.CharField(max_length=25)
    num_CIN = models.CharField(max_length=25)
    sexe = models.CharField(max_length=25, null=True, choices=SEXE)

    def __str__(self):
        return self.nom

class Activite(models.Model) :
    activite = models.CharField(max_length=30, null=True)
    

    def __str__(self):
        return self.activite


class Operation(models.Model) :
    STATUS = (
        ('Payé', 'Payé'),
        ('Non payé', 'Non payé'),
    )

    activite = models.ForeignKey(Activite, null=True, on_delete=models.SET_NULL)
    tarif = models.PositiveBigIntegerField(null=True)
    date_operation = models.DateTimeField(default=datetime.now)
    quantite = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=25, null=True, choices=STATUS)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    @property
    def Montant (self):
        montant = self.tarif * self.quantite
        return montant

    @property
    def Dette (self) :
        Dette = 0
        if self.status == 'Non payé':
            Dette = self.tarif * self.quantite
        return Dette
    @property
    def Caisse (self) :
        caisse = 0
        if self.status == 'Payé' : 
            caisse = self.tarif * self.quantite
        return caisse


class Abonnement(models.Model) :
    STATUS = (
        ('Payé', 'Payé'),
        ('Non payé', 'Non payé'),
    )

    debut = models.DateField (null=True)
    fin = models.DateField(null=True)
    status = models.CharField(max_length=25, null=True, choices=STATUS)
    clients = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    dateDePayement = models.DateField(null=True)

    def ___date___(self):
        return self.fin