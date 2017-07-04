# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# importar modelo
from documentos.models import Documento

#crear subclase de admin.ModelAdmin
class DocumentoAdmin(admin.ModelAdmin):
	model = Documento

#Registrar MOdelAdmin para cada modelo

admin.site.register(Documento,DocumentoAdmin)
