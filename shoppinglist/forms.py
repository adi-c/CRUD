from django import forms  
from shoppinglist.models import Shoppinglist  
class ShoppinglistForm(forms.ModelForm):  
    class Meta:  
        model = Shoppinglist  
        fields = "__all__"  