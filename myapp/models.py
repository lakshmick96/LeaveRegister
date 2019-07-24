from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	name = models.CharField(max_length=300)
	Employee_first_name = models.CharField(max_length=100, default='')
	Middle_name = models.CharField(max_length=100, default='', blank=True)
	Employee_last_name = models.CharField(max_length=100, default='')
	email = models.EmailField()
	ph_no = models.CharField(max_length=10)
	emp_type = models.CharField(max_length=10, choices=[('Manager', 'Manager'),
										('Employee', 'Employee'),
										])
	user_status = models.CharField(max_length=10, default='Active', choices=[('Active', 'Active'),
														('Inactive', 'Inactive')])
class Mapping(models.Model):
	Employee = models.ManyToManyField(CustomUser, related_name='user_as_employee')
	Manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class LeaveRequest(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	From = models.DateField(auto_now=False, auto_now_add=False)
	To = models.DateField(auto_now=False, auto_now_add=False)
	LeaveType = models.CharField(max_length=10, choices=[('Casual', 'Casual'),
														('Sick', 'Sick'),
														('Comp off', 'Comp off')])
	Reason = models.TextField(max_length=500)
	Status = models.BooleanField(default=None, null=True)

