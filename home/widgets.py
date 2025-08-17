from django import forms
from django.utils.safestring import mark_safe
class MyInputWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe('<input type="text" name="%s" value="%s" />' % (name, self.format_value(value)))
    class Media:
        css = {}
        js = (
            '/static/js/jquery-1.10.2.min.js',
        )