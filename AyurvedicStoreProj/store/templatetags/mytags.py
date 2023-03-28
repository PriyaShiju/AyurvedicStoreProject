from django import template

register = template.Library()

time_format="%A, %B %d, %Y at %I:%M%p"
time_format_mil ="%A, %B %d, %Y at %H:%M%p"

def mydate(oldvalue, miltime=False):
    #return oldvalue
    if miltime : return oldvalue.strftime(time_format_mil).upper()
    return oldvalue.strftime(time_format)

register.filter('mydate', mydate)

