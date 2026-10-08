from django.shortcuts import render
from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.filter(
    is_published=True,
    is_on_main=True,
).select_related('wrapper', 'category').order_by('title')
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)