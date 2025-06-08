from django.contrib import admin

from core.models.Medico import Medico
from core.models.Recepcionista import Recepcionista

# Register your models here.
admin.site.register(Medico)
admin.site.register(Recepcionista)

