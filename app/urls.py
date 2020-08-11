from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

# 	url(r'^user_client_management//$',$',views.demo_client_index,name='client_index'),

urlpatterns=[
################# DEMO URLS ################
# ================= USER DEMOS===========
	url(r'^user_demo/$',views.demo_user_index,name='user_index'),
	url(r'^user_bill_management/$',views.demo_bill_index,name='bill_index'),
	url(r'^user_location_management/$',views.demo_location_index,name='location_index'),
	url(r'^user_client_management/$',views.demo_client_index,name='client_index'),
	# url(r'^user_demo/$',views.demo_user_index,name='user_index'),

# # ===================== ADMIN DEMOS===========
	url(r'^demo_admin$',views.demo_admin_index,name='demo_admin_index'),
	# url(r'^$',views.user_dash,name='user_dash'),
	url('^$',views.user_dash,name='user_dash'),

# ##############################################
# 	url('^$',views.user_dash,name='user_dash'),
# 	url(r'^add_customer/$',views.add_customer,name='add_customer'),
# 	url(r'^all_customers/',views.all_customers,name='all_customers'),
# 	url(r'^customer/(\d+)',views.single_customer,name='single_customer'),
# 	url(r'^search/', views.search_results, name='search_results'),
# 	url(r'^customer_location/(\d+)$',views.customer_in_location,name='customer_in_location'),
# 	url(r'^add_location/$', views.add_location, name='add_location'),
	####################### new user urls ###################33
	# url('^$',views.user_dash,name='user_dash'),
	url(r'^paid$', views.paid_bills, name='paid_bills'),
	url(r'^pending$', views.pending_bills, name='pending_bills'),
	url(r'^single_location$', views.single_location, name='single_location'),
	url(r'^location_readings$', views.location_readings, name='location_readings'),
	url(r'^locations_pending$', views.locations_pending, name='locations_pending'),
# #################################### admin urls ###########################
	url(r'^homes_connected$', views.homes_connected, name='homes_connected'),
	url(r'^units_consumed$', views.units_consumed, name='units_consumed'),
	url(r'^meter_readings$', views.meter_readings, name='meter_readings'),
	url(r'^revenue_manager$', views.revenue_manager, name='revenue_manager'),
	url(r'^transactions_made$', views.transactions_made, name='transactions_made'),
	url(r'^payments_location$', views.payments_location, name='payments_location'),
	url(r'^payments_single_location$', views.payments_single_location, name='payments_single_location'),
	url(r'^pending_payments$', views.pending_payments, name='pending_payments'),
	url(r'^pending_per_location$', views.pending_per_location, name='pending_per_location'),
	url(r'^units_per_location$', views.units_per_location, name='units_per_location'),
	url(r'^connected_per_location$', views.connected_per_location, name='connected_per_location'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

