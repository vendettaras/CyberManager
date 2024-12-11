from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Client.views import abonnement_ajout, index, client_ajout, client_detail, client_modifier, client_effacer, operation_index, operation_ajout, rendement

urlpatterns=[
    
    path('', index, name="index"),
    path('ajout/', client_ajout, name='ajout'),
    path('client/<str:pk_test>', client_detail, name='client'),
    path('modifier/<str:pk>/', client_modifier, name='modifier'),
    path('effacer/<str:pk>/',client_effacer , name='effacer'),
    # path('variation/', variation, name='tarif'),
    path('ajoutOperation/<str:pk>/', operation_ajout, name='operation_ajout'),
    path('ajoutAbonnement/<str:pk>/', abonnement_ajout, name='abonnement_ajout'),
    path('operationDetail/', operation_index, name='operation_index'),
    path('rendement/', rendement, name='rendement')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)