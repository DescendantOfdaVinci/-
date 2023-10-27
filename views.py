from django.shortcuts import render

from .models import *
def show_products(request):
    context = {'product': Product.objects.all()}

    return render(request, 'vivod.html', context=context)


def show_user(request):
    context = {'purchaser': Purchaser.objects.all()}

    return render(request, 'something.html', context=context)

