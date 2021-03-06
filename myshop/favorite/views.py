from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from shop.models import Product, Category
from .favorite import Favorite
from .forms import FavoriteAddProductForm


@require_POST
def favorite_add(request, product_id):
    favorite = Favorite(request)
    product = get_object_or_404(Product, id=product_id)
    form = FavoriteAddProductForm(request.POST)
    if form.is_valid():
        favorite.add(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def favorite_remove(request, product_id):
    favorite = Favorite(request)
    product = get_object_or_404(Product, id=product_id)
    favorite.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def favorite_detail(request):
    categories = Category.objects.all()
    favorite = Favorite(request)
    return render(request, 'favorite/detailfav.html', {"categories": categories, 'favorite': favorite})