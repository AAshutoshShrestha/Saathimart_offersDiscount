from django.contrib import admin
# Register your models here.
from .models import category,offers_by_category,offers_by_product


admin.site.index_title = 'Welcome to Admin Dashboard'

class category_list(admin.ModelAdmin):
    list_display = ('id','name','icon',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(category,category_list)

class offerBYcatlist(admin.ModelAdmin):
    list_display = ('category','discount','start_date','end_date','status',)
    list_filter = ('category',)
    search_fields =('category','discount','start_date','end_date','status',)
    list_per_page = 15

admin.site.register(offers_by_category,offerBYcatlist)

class offerBYprodlist(admin.ModelAdmin):
    list_display = ('category','product_name','MRP','discount_rate','start_date','end_date','status',)
    list_filter = ('category','product_name',)
    search_fields =('category','product_name','MRP','discount_rate','start_date','end_date','status',)
    list_per_page = 15

admin.site.register(offers_by_product,offerBYprodlist)