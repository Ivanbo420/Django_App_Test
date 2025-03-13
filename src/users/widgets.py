from django.forms import widgets
from django.utils.safestring import mark_safe

class CustomImageField(widgets.FileInput):
    def render(self, name, value, attrs= None, **kwargs):
        default_html= super().render(name, value, attrs, **kwargs)
        img_html= mark_safe(f'<img src="{value.url}" width="100" />')
        return f'{img_html}{default_html}'