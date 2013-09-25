from django import forms
from models import *

class NcAddForm(forms.ModelForm):
    class Meta:
        model = Nonconformity
        fields = ('title', 'description', 'reproduction', 'expected')

class NcEditForm(forms.ModelForm):
    class Meta:
        model = Nonconformity
        exclude = ('author',)

class NcSearchForm(forms.Form):
    status = forms.ModelMultipleChoiceField(queryset=Status.objects.exclude(is_close=True), required=False)
