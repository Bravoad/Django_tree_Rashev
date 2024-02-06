from django import template
from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(parent=None)
    full_menu = get_full_menu(menu_items, current_url)
    return {'menu_items': full_menu}

def get_full_menu(menu_items, current_url):
    full_menu = []
    for item in menu_items:
        active = item.url == current_url
        children = get_full_menu(MenuItem.objects.filter(parent=item), current_url)
        full_menu.append({
            'name': item.name,
            'url': item.url,
            'active': active,
            'children': children,
        })
    return full_menu