from django.forms.widgets import MultiWidget, Select

class ProductAttributeValueWidget(MultiWidget):
    def __init__(self, attrs=None):
        widgets = []
        widgets.append(Select(attrs=attrs))
        super().__init__(widgets, attrs)

    def decompress(self, value):
        pass

    def compress(self, value):
        pass

