from django.core.exceptions import ValidationError
import re
import datetime

def validate_desired_time(value) :
    desired_time= str(value)
    if not re.match("^[A-Za-z 0-9]*$", desired_time):
        raise ValidationError("enter a valid desired time")
    return value

def validate_startdate(value):
    startdate = value
    if startdate < datetime.date.today():
        raise ValidationError("The date cannot be in the past!")
    return startdate

def validate_desired_budget_max(value):
    def clean(self):
        data=self.cleaned_data
        self.desired_budget_max = data['self.desired_budget_max']
        self.desired_budget_min = data['self.desired_budget_min']
        if self.desired_budget_max < self.desired_budget_min :
            raise ValidationError("the max should be greater than min")
        return data














