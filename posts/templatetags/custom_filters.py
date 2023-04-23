from django import template

register = template.Library()

@register.filter
def orderby_date(queryset, order):
    if order == 'asc':
        return queryset.order_by('created')
    elif order == 'desc':
        return queryset.order_by('-created')
    else:
        return queryset
