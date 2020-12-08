from django import template

register=template.Library()


@register.filter(name="currencys")
def currencys(number):
    return "₹ "+str(number)
   