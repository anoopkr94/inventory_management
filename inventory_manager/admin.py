from django.contrib import admin
from .models import category,item,purchase,sale,cartitem

class productAdmin(admin.ModelAdmin):
    list_display = ('name','brand','size','price','mrp','stock')
class purchaseAdmin(admin.ModelAdmin):
    list_display = ('name','brand','price','mrp','qty','total')
class saleAdmin(admin.ModelAdmin):
    list_display = ('name','brand','mrp','qty','total')

admin.site.register(item,productAdmin)
admin.site.register(category)
admin.site.register(cartitem)
admin.site.register(purchase,purchaseAdmin)
admin.site.register(sale,saleAdmin)
# Register your models here.
