from django import template

register = template.Library()

@register.filter
def filter_priority(items, priority):
    """Filter items by priority level"""
    return [item for item in items if item.get('priority', '').lower() == priority.lower()]


@register.filter
def sub(value, arg):
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return ''
