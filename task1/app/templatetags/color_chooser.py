from django import template

register = template.Library()


@register.filter(name='color')
def color_chooser(value):
    try:
        value = float(value)
    except ValueError:
        return ''
    if value < 0:
        return 'green'
    elif 1 <= value < 2:
        return 'LightSalmon'
    elif 2 <= value < 5:
        return 'Red'
    elif value >= 5:
        return 'DarkRed'
    else:
        return ''
