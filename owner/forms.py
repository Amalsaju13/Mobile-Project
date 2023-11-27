from django import forms
from owner.models import Mobiles
from customer.forms import Orders


# class MobileForm(forms.Form):
#     brand = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     specification = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     ram = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     strorage = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#     quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         price = cleaned_data.get("price")
#         quantity = cleaned_data.get("quantity")
#         if price < 0:
#             msg = "invalid price"
#             self.add_error("price", msg)
#         if quantity < 0:
#             msg = "invalid quantity"
#             self.add_error("quantity", msg)

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = "__all__"
        widgets = {
            "brand":forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "specification":forms.TextInput(attrs={"class": "form-control"}),
            "ram":forms.TextInput(attrs={"class": "form-control"}),
            "storage":forms.TextInput(attrs={"class": "form-control"}),
            "price":forms.NumberInput(attrs={"class": "form-control"}),
            "quantity":forms.NumberInput(attrs={"class": "form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }

class OrderEditForm(forms.ModelForm):
    options = (
        ("order_placed", "order_placed"),
        ("dispatched", "dispatched"),
        ("in_transit", "in_transit"),
        ("delivered", "delivered"),
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"}))
    class Meta:
        model=Orders
        fields=[
            "expected_delivery_date","status"
        ]
        widgets={
            "expected_delivery_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "status":forms.Select(attrs={"class":"form-select"})
        }
