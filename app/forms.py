from django import forms
from .models import Customer,Meter_Reading,Location

class Customer_Form(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = ['product']

class Meter_Reading_Form(forms.Form):
	class Meta:
		current_reading = forms.IntegerField()

class Location_Form(forms.ModelForm):
	class Meta:
		model = Location
		exclude = ['date_read']

		# def __init__(self, *args, **kwargs):
		# 	super(Location_Form, self).__init__(*args, **kwargs)
		# # 	# self.fields['house_name']=forms.CharField(max_length=15)
		# # 	# self.fields['zone']=forms.CharField(max_length=15)
		# # 	# self.fields['court']=forms.CharField(max_length=15)
		# 	self.queryset = forms.ModelChoiceField(queryset=Meter_Reading.objects.all(label="control_reading"))
		# 	# self.fields['meter_reading']=forms.ModelChoiceField(queryset=Meter_Reading.objects.all(label="add_readings"))

# class Location_Meter_Form(forms.Form):
# 	current_reading = forms.IntegerField()