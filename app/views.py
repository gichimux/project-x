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

# # ============== ADMIN ===========
def demo_admin_index(request):
	return render(request,'admino/index.html' )


# #########################################

@login_required(login_url='/accounts/login/')
def user_dash(request):
	# current_user = request.user
	# locations = Location.objects.all()
	return render(request, 'dash/index.html', {})

# @login_required(login_url='/accounts/login/')
# def add_customer(request):	
# 	# current_user = request.user
# 	if request.method == 'POST':
# 		form = Customer_Form(request.POST, request.FILES)
# 		if form.is_valid():
# 			add_customer = form.save(commit=False)
# 			# add_customer.user = current_user
# 			add_customer.save()
# 		return redirect('user_dash')
# 	else:
# 		form = Customer_Form()
# 	return render(request, 'dash/add_customer.html', {"form":form})

# @login_required(login_url='/accounts/login/')
# def all_customers(request):
# 	all_customers = Customer.fetch_all_customers()
# 	return render(request, 'dash/all_customers.html',{"all_customers": all_customers})

# @login_required(login_url='/accounts/login/')
# def single_customer(request, customer_id):
# 	single_customer = Customer.get_single_customer(customer_id)
# 	return render(request, 'dash/single_customer.html', {"single_customer": single_customer})

# @login_required(login_url='/accounts/login/')
# def search_results(request):
	
# 	if 'location' in request.GET and request.GET['location']:
# 		search_term =request.GET.get('location')
# 		searched_location = Location.search_location(search_term)
# 		message = f'{search_term}'

# 		# if searched_location is customer_location:
# 		return render(request, 'dash/search.html',{"message":message, "locations": searched_location})
# 	else:
# 		message = "You haven't searched for any term"
# 		return render(request, 'dash/search.html', {"message":message})
# 	# return redirect('customer_in_location')

# @login_required(login_url='/accounts/login/')
# def customer_in_location(request,id):
# 	locations = Location.objects.get(id=id)
# 	customers = Customer.objects.filter(location=id)
# 	# meter_reading = Meter_Reading.objects.get(id=id)
# 	# x = meter_reading.units_used()
# 	if request.method == 'POST':
# 		form = Meter_Reading_Form(request.POST, request.FILES)
# 		if form.is_valid():
# 			add_reading=form.save(commit=False)
# 			# x = add_reading.current_reading - add_reading.initial_reading
# 			add_reading.customer = customers
# 			# add_reading.units_consumed +=x
# 			# add_reading.location = locations
# 			add_reading.save()
			
# 			return redirect ('user_dash')
# 	else:
# 		form = Location_Meter_Form()
# 	return render(request, 'dash/customer_in_location.html', {"customers":customers,"locations":locations, "form": form})

# @login_required(login_url='/accounts/login/')
# def add_location(request):
# 	if request.method == 'POST':
# 		form = Location_Form(request.POST, request.FILES)
# 		if form.is_valid():
# 			add_location = form.save(commit=False)
# 			add_location.save()
# 		return redirect ('user_dash')
# 	else:
# 		form = Location_Form()
# 	return render (request, 'dash/add_location.html', {"form":form})

# 	######################## new views ################################3

# @login_required(login_url='/accounts/login/')
# def all_locations(request):
#     locations = Location.objects.all()
#     if request.method == 'POST':
#         form = New_Location(request.POST, request.FILES)
#         if form.is_valid():
#             location=form.save(commit=False)
#             location.save() 
#             return redirect(all_locations)
#     else:
#         form =NewDistributor()
#     return render(request,'user/location_management/location_index.html',{'locations':location,'form':form})

# @login_required(login_url='/accounts/login/')
# def single_location(request,id):
#     location = Location.objects.get(id=id)
#     customers = Customer.objects.filter(location=id)
#     if request.method == 'POST':
#         form = New_Customer(request.POST, request.FILES)
#         if form.is_valid():
#             customer=form.save(commit=False)
#             customer.location = location
#             customer.save() 
#             return redirect(single_locations)
#     else:
#         form =New_Customer()
#     return render(request,'user/location_management/single_location.html',{'house':house,'categories':categories})


# @login_required(login_url='/accounts/login/')
# def all_customers(request):
# 	all_customers = Customer.fetch_all_customers()
# 	return render(request, 'client_management/client_index.html',{"all_customers": all_customers})

# @login_required(login_url='/accounts/login/')
# def single_customer(request, id):
# 	customer = Customer.objects.get(id=id)
# 	meter_readings = Meter_Reading.objects.filter(customer=id)
# 	if request.method == 'POST':
# 		form = Meter_Reading_Form(request.POST, request.FILES)
# 		if form.is_valid():
# 			reading=form.save(commit=False)
# 			reading.customer = customer
# 			customer.save()
# 			return redirect(single_customer)
# 		else:
# 			form =Meter_Reading_Form()
# 	return render(request, 'client_management/single_customer.html',{"all_customers": all_customers})

@login_required(login_url='/accounts/login/')
def paid_bills(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'user/bill_management/paid.html',{})

@login_required(login_url='/accounts/login/')
def pending_bills(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'user/bill_management/pending.html',{})

@login_required(login_url='/accounts/login/')
def single_location(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'user/location_management/single_location.html',{})

@login_required(login_url='/accounts/login/')
def location_readings(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'user/location_management/location_readings.html',{})

@login_required(login_url='/accounts/login/')
def locations_pending(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'user/location_management/locations_pending.html',{})

############ADMIN VIEWS################

@login_required(login_url='/accounts/login/')
def homes_connected(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/customer_management/customer_index.html',{})

@login_required(login_url='/accounts/login/')
def connected_per_location(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/customer_management/connected_homes_per_location.html',{})


@login_required(login_url='/accounts/login/')
def units_consumed(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/units_management/units_index.html',{})


@login_required(login_url='/accounts/login/')
def units_per_location(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/units_management/units_per_location.html',{})


@login_required(login_url='/accounts/login/')
def meter_readings(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/meter_readings/meter_readings_index.html',{})

@login_required(login_url='/accounts/login/')
def revenue_manager(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/revenue_management/revenue_index.html',{})

@login_required(login_url='/accounts/login/')
def transactions_made(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/revenue_management/transactions.html',{})

@login_required(login_url='/accounts/login/')
def payments_location(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/revenue_management/payments_location.html',{})

@login_required(login_url='/accounts/login/')
def payments_single_location(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/revenue_management/payment_single_location.html',{})

@login_required(login_url='/accounts/login/')
def pending_payments(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/revenue_management/pending_payments.html',{})

@login_required(login_url='/accounts/login/')
def pending_per_location(request):
	# all_customers = Customer.fetch_all_customers()
	return render(request, 'admino/revenue_management/pending_per_location.html',{})
