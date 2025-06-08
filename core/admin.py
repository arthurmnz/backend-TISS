from django.contrib import admin

from core.models.Medico import Medico
from core.models.Recepcionista import Recepcionista
from core.models.Clinica import Clinica
from core.models.Paciente import Paciente

# Register your models here.
admin.site.register(Medico)
admin.site.register(Recepcionista)
admin.site.register(Clinica)
admin.site.register(Paciente)
