from django import template

register = template.Library()

@register.filter()
def match_str(path_param, pattern):
    print(f"path_param = {path_param}")
    if path_param == pattern:
        return True
    return False