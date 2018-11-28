from django import template
register = template.Library()


@register.simple_tag()
def spliceUrl(urlstr):
    return '/rangoapp/category/{0}'.format(urlstr)
