from __future__ import absolute_import
from __future__ import print_function
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser, LeaveRequest


class AddUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'Employee_first_name', 'Middle_name', 'Employee_last_name', 'email', 'ph_no', 'emp_type')

    # def __init__(self, *args, **kwargs):
    # 	super(AddUserForm, self).__init__(*args, **kwargs)
    # 	self.fields['middle_name'].required = False


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
        'Employee_first_name', 'Middle_name', 'Employee_last_name', 'email', 'ph_no', 'emp_type', 'user_status')

    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            print("Validation failed")
            raise ValidationError("First name is required.")
        return self.cleaned_data["first_name"]

    # def clean_last_name(self):
    # 	if self.cleaned_data["last_name"].strip() == '':
    # 		raise ValidationError("Last name is required.")
    # 	return self.cleaned_data["last_name"]
