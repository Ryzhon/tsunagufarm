from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Shop
from decouple import config
import json


def show_shops(request):
    shops = request.user.bought_shops.all()
    page_title = "ショップ一覧"
    css_url = "styles.css"
    return render(request, 'shops.html', {"shops": shops,"page_title":page_title,"css_url": css_url})

def show_user_with_shop(request):
    shops = request.user.bought_shops.all()
    page_title = "つながった農家一覧"
    css_url = "styles.css"
    return render(request, 'shops.html', {"shops": shops,"page_title":page_title,"css_url": css_url})

def show_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    context = {
        'header_text': 'Dynamic Header Text from View',
        'page_title': f'{shop.name}のレシピ',
        'shop': shop
    }
    return render(request, 'shop.html', context)

def create_shop(request):
    GOOGLE_MAP_API_KEY = config('GOOGLE_MAP_API_KEY', default='')
    if request.method == "POST":
        name = request.POST.get('name')
        img = request.POST.get('img')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if name and img and latitude and longitude:
            Shop.objects.create(
                name=name,
                img=img,
                latitude=float(latitude),
                longitude=float(longitude),
                owner=request.user
            )
            return redirect('/map')

    context = {
        "page_title":"店舗作成",
        'API_KEY': GOOGLE_MAP_API_KEY,
    }
    return render(request, "add_farm.html",context)

@login_required
def map(request):
    GOOGLE_MAP_API_KEY = config('GOOGLE_MAP_API_KEY', default='')
    user_has_shop = Shop.objects.filter(owner=request.user).exists()

    shops = Shop.objects.all()
    shops_data = [{'name': shop.name, 'img': shop.img.url, 'latitude': shop.latitude, 'longitude': shop.longitude, 'id':shop.id} for shop in shops]
    context = {
        'page_title': 'つなぐファーム',
        'API_KEY': GOOGLE_MAP_API_KEY,
        'shops': json.dumps(shops_data),
        'user_has_shop': user_has_shop,
    }

    return render(request, 'map.html', context)

def other(request):
    context={
        "page_title":"その他"
    }
    return render(request, "others.html", context)
