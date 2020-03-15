from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime 


# ##### DEMO VIEWS #########
#============== USER ===========
def demo_user_index(request):
	return render(request,'user/index.html' )

def demo_bill_index(request):
	return render(request,'user/bill_management/bill_index.html' )

def demo_location_index(request):
	return render(request,'user/location_management/location_index.html' )

def demo_client_index(request):
	return render(request,'user/client_management/client_index.html' )

# ============== ADMIN ===========
def demo_admin_index(request):
	return render(request,'admin/index.html' )


#########################################

@login_required(login_url='/accounts/login/')
def user_dash(request):
	# current_user = request.user
	locations = Location.objects.all()
	return render(request, 'dash/index.html', {"locations":locations})

@login_required(login_url='/accounts/login/')
def add_customer(request):	
	# current_user = request.user
	if request.method == 'POST':
		form = Customer_Form(request.POST, request.FILES)
		if form.is_valid():
			add_customer = form.save(commit=False)
			# add_customer.user = current_user
			add_customer.save()
		return redirect('user_dash')
	else:
		form = Customer_Form()
	return render(request, 'dash/add_customer.html', {"form":form})

@login_required(login_url='/accounts/login/')
def all_customers(request):
	all_customers = Customer.fetch_all_customers()
	return render(request, 'dash/all_customers.html',{"all_customers": all_customers})

@login_required(login_url='/accounts/login/')
def single_customer(request, customer_id):
	single_customer = Customer.get_single_customer(customer_id)
	return render(request, 'dash/single_customer.html', {"single_customer": single_customer})

@login_required(login_url='/accounts/login/')
def search_results(request):
	
	if 'location' in request.GET and request.GET['location']:
		search_term =request.GET.get('location')
		searched_location = Location.search_location(search_term)
		message = f'{search_term}'

		# if searched_location is customer_location:
		return render(request, 'dash/search.html',{"message":message, "locations": searched_location})
	else:
		message = "You haven't searched for any term"
		return render(request, 'dash/search.html', {"message":message})
	# return redirect('customer_in_location')

@login_required(login_url='/accounts/login/')
def customer_in_location(request,id):
	customers = Customer.objects.filter(location=id)
	locations = Location.objects.get(id=id)
	meter_reading = Meter_Reading.objects.get(id=id)
	x = meter_reading.current_reading-meter_reading.previous_reading
	# units_used = meter_reading.units_used()
	if request.method == 'POST':
		form = Meter_Reading_Form(request.POST, request.FILES)
		if form.is_valid():
			current_reading = form.cleaned_data['current_reading']
			add_reading = meter_reading(current_reading = current_reading)
			add_reading=form.save()
			add_reading.save
			
		return redirect ('user_dash')
	else:
		form = Meter_Reading_Form()
	return render(request, 'dash/customer_in_location.html', {"customers":customers,"locations":locations, "units_used": x, "form": form})

@login_required(login_url='/accounts/login/')
def add_location(request):
	if request.method == 'POST':
		form = Location_Form(request.POST, request.FILES)
		if form.is_valid():
			add_location = form.save()
			add_location.save()
		return redirect ('user_dash')
	else:
		form = Location_Form()
	return render (request, 'dash/add_location.html', {"form":form})