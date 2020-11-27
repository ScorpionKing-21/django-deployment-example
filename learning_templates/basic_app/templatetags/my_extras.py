from django import template

register = template.Library()

@register.filter(name='sub')
def sub(value,arg):
    """
    subtracts arg from value
    """
    value = int(value)-int(arg)
    return value

# register.filter('sub',sub)
