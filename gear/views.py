from django.shortcuts import render, get_object_or_404, redirect
from .models import Gear, GearBooking
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import CartItem 

def gear_list(request):
    gears = Gear.objects.all()
    return render(request, 'gear/gear_list.html', {'gears': gears})


@login_required
def gear_detail(request, gear_id):
    gear = get_object_or_404(Gear, id=gear_id)
    if request.method == 'POST':
        size = request.POST.get('size')
        trek_name = request.POST.get('trek_name')
        trek_date = request.POST.get('trek_date')
        quantity = int(request.POST.get('quantity', 1))
        total_price = gear.price * quantity

        booking = GearBooking.objects.create(
            user=request.user,
            gear=gear,
            size=size,
            trek_name=trek_name,
            trek_date=datetime.strptime(trek_date, '%Y-%m-%d'),
            quantity=quantity,
            total_price=total_price
        )
        return redirect('gear_checkout', booking_id=booking.id)

    return render(request, 'gear/gear_detail.html', {'gear': gear})

def order_confirmation(request):
    return render(request, 'gear/order_confirmation.html')

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.gear.price * item.quantity for item in cart_items)
    return render(request, 'gear/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart_view(request, gear_id):
    if request.method == "POST":
        gear = get_object_or_404(Gear, id=gear_id)
        size = request.POST.get("size", "Not Required")
        trek_name = request.POST.get("trek_name")
        trek_date = request.POST.get("trek_date")
        quantity = int(request.POST.get("quantity", 1))

        CartItem.objects.create(
            user=request.user,
            gear=gear,
            size=size,
            quantity=quantity,
            trek_date=trek_date,
            trek_name=trek_name
        )

        return redirect('cart')
    print(request.POST)
@login_required
def checkout(request, booking_id):
    booking = get_object_or_404(GearBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        return redirect('order_confirmation')
    return render(request, 'gear/gear_checkout.html', {'booking': booking})
@login_required
def cart_checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.gear.price * item.quantity for item in cart_items)

    return render(request, 'gear/cart_checkout.html', {'cart_items': cart_items, 'total': total})


@login_required
def delete_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')  # Redirects back to cart view

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    for item in cart_items:
        GearBooking.objects.create(
            user=request.user,
            gear=item.gear,
            size=item.size,
            trek_name=item.trek_name,
            trek_date=item.trek_date,
            quantity=item.quantity,
            total_price=item.quantity * item.gear.price
        )
    
    cart_items.delete()  # Clear cart after placing the order
    
    return redirect('order_confirmation')
def order_confirmation(request):
    return render(request, 'gear/order_confirmation.html')

@login_required
def dashboard(request):
    user_bookings = GearBooking.objects.filter(user=request.user).order_by('-trek_date')
    return render(request, 'gear/dashboard.html', {'user_bookings': user_bookings})

