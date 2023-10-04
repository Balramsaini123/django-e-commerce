from django.shortcuts import render, redirect
from app.models import slider, banner_area, Main_Category, Product


def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]
    main_category = Main_Category.objects.all().order_by('-id')
    product = Product.objects.filter(section__name = "top deal of the day")
    # print(product)
    context = {
        'sliders': sliders,
        'banners': banners,
        'main_category': main_category,
        'product': product,
    }
    return render(request, 'main/home.html', context)
