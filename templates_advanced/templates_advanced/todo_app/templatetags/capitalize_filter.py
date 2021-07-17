from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value, captalized_chars_count=1):
    return value[:captalized_chars_count].upper() + value[captalized_chars_count+1:].lower()
