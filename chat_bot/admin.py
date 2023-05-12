from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import chatFlow,question,answer,option

admin.site.register(question, admin.ModelAdmin)
admin.site.register(answer, admin.ModelAdmin)
admin.site.register(option, admin.ModelAdmin)
admin.site.register(chatFlow, MPTTModelAdmin)
