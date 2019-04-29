from django.contrib import admin

from inventory.models import Account, Owner

#admin.site.register(Account)
#admin.site.register(Owner)

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('owner', 'stbmodel','acct_num', 'stbmodel', 'rid', 'sid', 'security_status', 'notes')
    fields = ('owner','stbmodel','acct_num', 'rid', 'sid', 'security_status', 'notes')

# Register the admin class with the associated model
admin.site.register(Account, AccountAdmin)

class OwnerAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Owner, OwnerAdmin)
