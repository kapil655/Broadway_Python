from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from product.forms import ProductForms
from .models import Product
from django.contrib.auth.decorators import login_required

def product_view(request):
    return HttpResponse("<h1>This is product view</h1>")

def landing_page(request):
    context = {
        "name": "kapil",
        "naam": "कपिल",
    }
    return render(request, 'product/index.html', context)

def game_choice(request):
    return render(request, 'product/game.html')

def facebook(request):
    return render(request, 'product/facebook.html')

def hangman(request):
    return render(request, 'product/hangman.html')

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "product/product_list.html", context)


@login_required(login_url='/user/login')
def product_create(request):
    form = ProductForms()
    if request.method == "POST":
        form = ProductForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/product_list/')
    
    context = {
        "form": form
    }
    return render(request, 'product/create.html', context)

@login_required(login_url='/user/login')
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForms(instance=product)
    
    if request.method == "POST":
        form = ProductForms(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    context = {
        "form": form,
        "product": product
    }
    return render(request, 'product/update.html', context)

@login_required(login_url='/user/login')
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')