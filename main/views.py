from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import category,offers_by_category,offers_by_product
from .filters import CategoryWise,ProductWise


def bycategory(request):
    query_list = offers_by_category.objects.all()
    categoryFilter = CategoryWise(request.GET, queryset=query_list)
    offers = categoryFilter.qs 
    context = {
        'Offer' : offers,
        'filter': categoryFilter
    }
    return render(request, 'views/by_category.html',context)

def byproduct(request):
    query_list = offers_by_product.objects.all()
    categoryFilter = ProductWise(request.GET, queryset=query_list)
    offers = categoryFilter.qs  
    context = {
        'Offer' : offers,
        'filter': categoryFilter
    }
    return render(request, 'views/by_product.html',context)