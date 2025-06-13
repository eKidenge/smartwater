# analysis/templatetags/water_filters.py
from django import template

register = template.Library()

@register.filter
def pressure_percentage(value, arg):
    """
    Calculates percentage for pressure visualization
    Usage: {{ pressure|pressure_percentage:min_max }}
    """
    try:
        min_val, max_val = arg
        return ((value - min_val) / (max_val - min_val)) * 100
    except (TypeError, ZeroDivisionError):
        return 0