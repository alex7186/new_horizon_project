from django import template

# import time

register = template.Library()


@register.filter(name="reverse")
def reverse(projects):

    return projects[::-1]
