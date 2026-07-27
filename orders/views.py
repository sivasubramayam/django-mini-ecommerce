# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from cart.models import Cart
from .models import Order


@login_required
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.total_price,
        )

    cart_items.delete()

    return redirect("home")


from django.shortcuts import render

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)

    return render(
        request,
        "orders.html",
        {"orders": orders},
    )