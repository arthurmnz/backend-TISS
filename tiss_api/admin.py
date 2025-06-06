from django.contrib import admin
from tiss_api.models.Beneficiario import *
from tiss_api.models.Procedimento import *
from tiss_api.models.Contratado import  * 
from tiss_api.models.Profissional import *
from tiss_api.models.Guias import *
from tiss_api.models.Procedimento import *

# Register your models here.
admin.site.register(Contratado)
admin.site.register(Profissional)
admin.site.register(Beneficiario)
admin.site.register(Procedimento)
# admin.site.register(ProcedimentoRealizado)
# admin.site.register(ProcedimentosSolicitados)
admin.site.register(GuiaConsulta)
# admin.site.register(GuiaSPSADT)