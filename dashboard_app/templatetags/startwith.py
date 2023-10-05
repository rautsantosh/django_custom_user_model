from django import template

register = template.Library()

@register.filter('startwith')
def startwith(text, starts):  # sourcery skip: assign-if-exp, reintroduce-else
    if isinstance(text, str):
        return text.startswith(starts)
    return False