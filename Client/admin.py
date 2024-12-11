from django.contrib import admin

from Client.models import Client, Activite, Operation

# Register your models here.

admin.site.register([Client, Activite, Operation])
