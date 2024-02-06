from django import template
from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(parent=None)
    for item in menu_items:
        item.active = item.url == current_url
        item.children = MenuItem.objects.filter(parent=item)
    return {'menu_items': menu_items}