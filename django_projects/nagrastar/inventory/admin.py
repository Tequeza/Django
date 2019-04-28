from django.contrib import admin

# Register your models here.
from inventory.models import Account, Owner, STBModel, AccountInstance

#admin.site.register(Account)
#admin.site.register(Owner)
#admin.site.register(STBModel)
#admin.site.register(AccountInstance)



class AccountAdmin(admin.ModelAdmin):
    list_display = ('acct_num', 'owner')

# Register the admin class with the associated model
admin.site.register(Account, AccountAdmin)

# Register the Admin classes for BookInstance using the decorator
@admin.register(AccountInstance) 
class AccountInstanceAdmin(admin.ModelAdmin):
    pass


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


# Register the admin class with the associated model
admin.site.register(Owner, OwnerAdmin)


class STBModelAdmin(admin.ModelAdmin):
    list_display = ('stbmodel', 'rid', 'sid')


# Register the admin class with the associated model
admin.site.register(STBModel, STBModelAdmin)
