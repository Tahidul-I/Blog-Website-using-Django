from django import template
register = template.Library()

def word_limiter(value):
    return value[0:500]

register.filter('custom_filter',word_limiter)