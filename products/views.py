from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    query = request.GET.get("q")
    category_id = request.GET.get("category")

    products = Product.objects.filter(is_available=True)

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, "home.html", {
        "products": products,
        "categories": categories
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {"product": product})