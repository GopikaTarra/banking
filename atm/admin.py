from django.contrib import admin
from .models import Account,Transaction

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'balance')
    search_fields = ('account_number',)

admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction)