from django import forms
import unrest_schema

from .models import Bar, Pose

@unrest_schema.register
class PoseForm(forms.ModelForm):
    USER_CAN_POST = 'ALL'
    USER_CAN_PUT = 'ALL'
    class Meta:
        model = Pose
        fields = ('name', 'limb', 'slug')


@unrest_schema.register
class BarForm(forms.ModelForm):
    data = forms.CharField(widget = forms.HiddenInput(), required = False)
    USER_CAN_POST = 'ALL'
    USER_CAN_PUT = 'ALL'
    class Meta:
        model = Bar
        fields = ('name', 'data')
