
"""Custom template tags for form rendering in CRUD app."""

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='add_class')
def add_class(field, css_class):
    """Add a CSS class to a form field widget."""
    return field.as_widget(attrs={**field.field.widget.attrs, 'class': css_class})


@register.filter(name='render_form')
def render_form(form):
    """Render a Django form as a table with safe HTML output."""
    return mark_safe(form.as_table())
