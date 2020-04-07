import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '..',)))
from django import template
from Kiosk.models import Food, OrderLine, Order
register = template.Library()

@register.simple_tag

def return_price(request):
    food = request.get('food')
    fp = [a['price'] for a in Food.objects.filter(pk=food).value('price')]
    fp_1 = fp[1]
    print('something')
    return fp_1

def return_quant(request):
    quant = request.get('quantity')
    q = [a['quantity'] for a in OrderLine.objects.filter(quantity=quant).value('quantity')]
    q_1 = q[1]
    return q_1
