from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from Client.forms import *
from Client.models import Abonnement, Client, Operation
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime

@login_required
def index(request):
    clients = Client.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        clients = Client.objects.filter(nom__icontains=item_name)
    operations = Operation.objects.all()

    totals = Operation.objects.raw('select id, date(date_operation), sum(tarif * quantite) as rend from client_operation WHERE date(date_operation)=date(now());')
    caisses = Operation.objects.raw('select id, date(date_operation), sum(tarif * quantite) as caissier from client_operation where date(date_operation)=date(now()) group by date(date_operation), status HAVING status="Payé";')
    dettes = Operation.objects.raw('select id, date(date_operation), sum(tarif * quantite) as dettier from client_operation where date(date_operation)=date(now()) group by date(date_operation), status HAVING status="Non payé";')
    
    # for o in totals:
    #     print(o.rend)
    # for i in caisses:
    #     print(i.caisse)
    # for i in dettes:
    #     print (i.dette)

    total = 0
    # caisses = 0
    # dettes = 0
    for operation in operations:
        total += operation.Montant
        # caisses += operation.Caisse
        # dettes += operation.Dette 
    return render(request, 'Client/index.html', context={"clients": clients, "operations": operations, "total": total, "caisses":caisses, "dettes":dettes, "date": datetime.now().date, 'totals': totals})

def rendement(request):
    rendement_journaliers = Operation.objects.raw('select id, date(date_operation), sum(tarif * quantite) as rend from client_operation group by date(date_operation);')
    caisse_journaliers = Operation.objects.raw('select id, date(date_operation), sum(tarif * quantite) as caisse from client_operation group by date(date_operation), status HAVING status="Payé";')
    dette_journaliers = Operation.objects.raw('select id, date(date_operation), sum(tarif * quantite) as dette from client_operation group by date(date_operation), status HAVING status="Non payé";')
    for o in rendement_journaliers:
        print(o.rend)
    for i in caisse_journaliers:
        print(i.caisse)
    for i in dette_journaliers:
        print (i.dette)
    return render(request, 'Client/rendement.html', context={"rendement_journaliers":rendement_journaliers, "caisse_journaliers":caisse_journaliers, "dette_journaliers":dette_journaliers})

@login_required
def client_ajout(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'Client/ajout.html',context = {'form': form})


def client_detail(request, pk_test ):
    client = Client.objects.get(id=pk_test)
    operations = client.operation_set.all()
    abonnements = client.abonnement_set.all()
    total = 0
    dettes =  0
    for operation in operations:
        total += operation.Montant
        dettes += operation.Dette
    return render(request, 'Client/detail_client.html', context={"client": client, "operations":operations, "total":total, "dettes":dettes, "abonnements":abonnements})

@login_required
def client_modifier(request, pk):

    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'Client/modifier.html', context={'form': form})

@login_required
def client_effacer(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('index')
    return render(request, 'Client/effacer.html', context={'item':client})

# def variation(request):
#     variations = Variation.objects.all()
#     return render(request, 'Client/prix.html', context={'variations':variations})

@login_required
def operation_ajout(request, pk):
    OperationFormSet = inlineformset_factory(Client, Operation,  fields=('activite', 'tarif', 'quantite', 'status',), extra=4)
    client = Client.objects.get(id=pk)
    formset = OperationFormSet(instance=client)
    if request.method == 'POST':
        formset = OperationFormSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    context = {"formset":formset}
    return render(request,'Client/vaovao.html',context)

def operation_index(request):
    operations = Operation.objects.all()
    total = 0
    caisses = 0
    dettes = 0
    for operation in operations:
        total += operation.Montant
        caisses += operation.Caisse
        dettes += operation.Dette
    return render(request, 'Client/operation_detail.html', context={"operations": operations ,"total":total, "caisses": caisses, "dettes":dettes })

def abonnement_ajout(request, pk):
    AbonnementFormSet = inlineformset_factory(Client, Abonnement,  fields=('debut', 'fin', 'status','dateDePayement'), extra=4)
    client = Client.objects.get(id=pk)
    formset = AbonnementFormSet(instance=client)
    if request.method == 'POST':
        formset = AbonnementFormSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    context = {"formset":formset}
    return render(request,'Client/abonnement.html',context)

