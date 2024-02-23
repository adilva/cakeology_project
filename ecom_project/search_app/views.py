from django.shortcuts import render
from ecom_app.models import Products
from django.db.models import Q

def SearchResult(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Products.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query':query,'product':product})
