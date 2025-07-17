from django.forms.widgets import MultiWidget, Select

class ProductAttributeValueWidget(MultiWidget):
    def __init__(self, attrs=None):
        widgets = []
        for attr_id , values in self.attribute_values_map.items():
            widgets.append(Select(attrs=attrs, choices=[(v.id, v.name) for v in values]))
        super().__init__(widgets, attrs)