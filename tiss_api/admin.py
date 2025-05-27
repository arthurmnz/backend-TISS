from django.contrib import admin
from .models import GuiaConsulta, GuiaSPSADT, Procedimento, Prestador, Paciente

# Register your models here.
admin.site.register(Prestador)
admin.site.register(Paciente)
admin.site.register(GuiaConsulta)
admin.site.register(GuiaSPSADT)
admin.site.register(Procedimento)