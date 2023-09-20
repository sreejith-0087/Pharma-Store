from django import forms
from staff.models import Medicine,Categories,Brand

categories=forms.ModelChoiceField(queryset=Categories.objects.all(),to_field_name='category')

class MedicineForm(forms.ModelForm):

    class Meta:
        model=Medicine
        fields="__all__"
        widgets={
            "medicine":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control",'rows':5}),

             "stock":forms.NumberInput(attrs={"class":"form-control"}),
        }

    # def sub_total(self):
    #     return self.product.price * self.quantity


