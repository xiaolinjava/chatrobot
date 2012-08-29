from django.contrib import admin

from jjechat.qAnda.models import QAndA

class QandaAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')
    list_filter = ('question', 'answer')
    
admin.site.register(QAndA, QandaAdmin)