from django import template

register=template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(x,cart):
    keys=cart.keys()
    print("this is products",x)
    print("this is keys",cart)
    for id in keys:
        if int(id) == x.id:
            return True

    return False

@register.filter(name='cart_quantity')
def cart_quantity(x,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == x.id:
            return cart.get(id)
    return False


@register.filter(name='cart_total')
def cart_total(x,cart):
    return x.price * cart_quantity(x,cart)


@register.filter(name='cart_last_total')
def cart_last_total(y,cart):
    sum=0;
    for p in y:
       
        sum += cart_total(p,cart)
    return sum

