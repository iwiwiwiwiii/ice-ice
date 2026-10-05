from django.shortcuts import render

from .models import IceCream


def ice_cream_list(request):
    context = {
        'ice_cream_catalog': IceCream.objects.filter(is_published=True),
    }
    return render(request, 'ice_cream/list.html', context)


def ice_cream_detail(request, pk):
    context = {
        'ice_cream': IceCream.objects.get(pk=pk),
    }
    return render(request, 'ice_cream/detail.html', context)