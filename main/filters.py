import django_filters
from .models import offers_by_category,offers_by_product

class CategoryWise(django_filters.FilterSet):
	class Meta:
		model = offers_by_category
		fields = ['category',]
		exclude = ['discount','status']


class ProductWise(django_filters.FilterSet):
	class Meta:
		model = offers_by_product
		fields =  ['category','product_name']
