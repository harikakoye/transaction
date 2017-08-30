from django.db import models
from.validate import *
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=15)
    transacton_status = models.CharField(max_length=20)
    transaction_propertytype_id = models.CharField(max_length=10)
    transaction_desired_time = models.CharField(max_length=20,validators=[validate_desired_time])
    transaction_customer_notes = models.TextField(max_length=30)
    transaction_agent_notes = models.TextField(max_length=50)
    transcation_active_duration = models.CharField(max_length=2)
    transaction_desired_budget_max = models.CharField(max_length=10, validators=[validate_desired_budget_max])
    transaction_desired_budget_min = models.CharField(max_length=10)
    transaction_startdate=models.DateField(max_length=20,validators=[validate_startdate])










