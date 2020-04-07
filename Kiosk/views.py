from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer,Food,Order,OrderLine
# Create your views here.
def main_menu(request):
    return render(request, 'Kioskapp/main_menu.html')

def viewcustomers(request):
    customer_objects = Customer.objects.all()
    return render(request, 'Kioskapp/viewcustomers.html', {'customers':customer_objects})

def viewcustomerorders(request,pk):
    customer_order_objects_qs = OrderLine.objects.filter(ord__cust_order__pk = pk)
    c = get_object_or_404(Customer, pk=pk)
    price_list = OrderLine.objects.filter(ord__cust_order__pk = pk).values_list('food__price', flat=True).order_by('id')
    quantity_list = OrderLine.objects.filter(ord__cust_order__pk = pk).values_list('quantity', flat=True).order_by('id')
    customer_order_objects = [c for c in customer_order_objects_qs]
    sub_total = [a*b for a,b in zip(price_list,quantity_list)]
    c_s_list = zip(customer_order_objects,sub_total)
    total = sum(sub_total)
    return render(request, 'Kioskapp/viewcustomerorders.html',
    {'c_s_list':c_s_list,'total':total, 'c':c})

def edit_customer(request, pk):
    if(request.method=="POST"):
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        Customer.objects.filter(pk=pk).update(name=name,address=address,city=city)
        return redirect('viewcustomers')
    else:
        c = get_object_or_404(Customer, pk=pk)
        return render(request,'Kioskapp/edit_customer.html',{'c':c})

def add_customer(request):
    if(request.method=="POST"):
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        Customer.objects.create(name=name,address=address,city=city)
        return redirect('viewcustomers')
    else:
        return render(request, 'Kioskapp/add_customer.html')

def viewfood(request):
    food_objects = Food.objects.all()
    return render(request,'Kioskapp/viewfood.html',{'food':food_objects})

def add_food(request):
    if(request.method=="POST"):
        food_name = request.POST.get('food_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Food.objects.create(food_name=food_name,description=description,price=price)
        return redirect('viewfood')
    else:
        return render(request, 'Kioskapp/add_food.html')

def edit_food(request, pk):
    if(request.method=="POST"):
        food_name = request.POST.get('food_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Food.objects.filter(pk=pk).update(food_name=food_name,description=description,price=price)
        return redirect('viewfood')
    else:
        f = get_object_or_404(Food, pk=pk)
        return render(request,'Kioskapp/edit_food.html',{'f':f})
      

def vieworders(request):
    order_objects_qs = OrderLine.objects.all()
    order_objects = [o for o in order_objects_qs]
    prices = OrderLine.objects.all().values_list('food__price', flat=True).order_by('id')
    quantity = OrderLine.objects.all().values_list('quantity', flat=True).order_by('id')
    subtotal = [a*b for a,b in zip(prices,quantity)]
    o_s_list = zip(order_objects,subtotal)
    return render(request,'Kioskapp/vieworders.html',
    {'order_objects':order_objects,'subtotal':subtotal, 'o_s_list':o_s_list})

def add_order(request):
    if(request.method=="POST"):
        cust_order = request.POST.get('cust_order')
        mode_payment = request.POST.get('mode_payment')
        # ord = request.POST.get('ord')
        food = request.POST.get('food')
        quantity = request.POST.get('quantity')
        ord = Order.objects.create(
            cust_order=Customer.objects.get(pk=cust_order),
            mode_payment=mode_payment
            )
        OrderLine.objects.create(
            ord=ord,
            food=Food.objects.get(pk=food),
            quantity=quantity
            )
        return redirect('vieworders')
    else:
        customer_objects = Customer.objects.all()
        food_objects = Food.objects.all()
        return render(request, 'Kioskapp/add_order.html',
        {'customer_objects':customer_objects,'food_objects':food_objects})

def delete_order(request,pk):
    Order.objects.filter(pk=pk).delete()
    OrderLine.objects.filter(pk=pk).delete()
    return redirect('vieworders')

def edit_order(request, pk):
    if(request.method=="POST"):
        cust_order_get = request.POST.get('cust_order')
        mode_payment_get = request.POST.get('mode_payment')
        # ord = request.POST.get('ord')
        food_get = request.POST.get('food')
        quantity_get = request.POST.get('quantity')
        Order.objects.filter(pk=pk).update(
            cust_order=Customer.objects.get(pk=cust_order_get),
            mode_payment=mode_payment_get
            )
        OrderLine.objects.filter(pk=pk).update(
            ord=Order.objects.get(pk=pk),
            food=Food.objects.get(pk=food_get),
            quantity=quantity_get
            )
        return redirect('vieworders')
    else:
        customer_objects = Customer.objects.all()
        food_objects = Food.objects.all()
        o = get_object_or_404(OrderLine, pk=pk)
        o_total = o.food.price * o.quantity
        return render(request, 'Kioskapp/edit_order.html',{'customer_objects':customer_objects,'food_objects':food_objects,'o':o,'o_total':o_total})