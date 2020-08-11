# from django import forms
# from .models import *

# class Customer_Form(forms.ModelForm):
# 	class Meta:
# 		model = Customer
# 		exclude = [] 


# # class Readings_Form(forms.ModelForm):
# # 	class Meta:
# # 		model = Bill 
# # 		exclude = ['location', '']

# class Location_Form(forms.ModelForm):
# 	class Meta:
# 		model = Location
# 		exclude = ['date_read', 'units_consumed']
# 		# meter_reading = model.ModelChoiceField(queryset=)

# 		# def __init__(self, *args, **kwargs):
# 		# 	super(Location_Form, self).__init__(*args, **kwargs)
# 		# # 	# self.fields['house_name']=forms.CharField(max_length=15)
# 		# # 	# self.fields['zone']=forms.CharField(max_length=15)
# 		# # 	# self.fields['court']=forms.CharField(max_length=15)
# 		# 	self.queryset = forms.ModelChoiceField(queryset=Meter_Reading.objects.all(label="control_reading"))
# 		# 	# self.fields['meter_reading']=forms.ModelChoiceField(queryset=Meter_Reading.objects.all(label="add_readings"))

# # class Location_Meter_Form(forms.Form):
# # 	current_reading = forms.IntegerField()
# class Location_Meter_Form(forms.ModelForm):
# 	class Meta:
# 		model = Location
# 		exclude = ['date_read', 'house_name', 'zone', 'court', 'house_number', 'initial_reading', 'units_consumed']

# ############# new forms ######################

# class New_Location(forms.ModelForm):
# 	class Meta:
# 		model = Location
# 		exclude = ['date_read', 'units_consumed']

# class New_Customer(forms.ModelForm):
# 	class Meta:
# 		model = Customer
# 		exclude = ['location'] 


# class Meter_Reading_Form(forms.ModelForm):
# 	class Meta:
# 		k/;pmodel= Meter_Reading
# 		# current_reading = forms.IntegerField()
# 		exclude =['previous_reading', 'customer', 'date_read']