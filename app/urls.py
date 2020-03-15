from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
################# DEMO URLS ################
# ================= USER DEMOS===========
	url(r'^user_demo/$',views.demo_user_index,name='user_index'),
	url(r'^user_bill_management/$',views.demo_bill_index,name='bill_index'),
	url(r'^user_location_management/$',views.demo_location_index,name='location_index'),
	url(r'^user_client_management/$',views.demo_client_index,name='client_index'),
	# url(r'^user_demo/$',views.demo_user_index,name='user_index'),

# ===================== ADMIN DEMOS===========
	url(r'^admin_demo$',views.demo_admin_index,name='admin_index'),
	# url(r'^$',views.user_dash,name='user_dash'),
	# url('^$',views.user_dash,name='user_dash'),

##############################################
	url('^$',views.user_dash,name='user_dash'),
	url(r'^add_customer/$',views.add_customer,name='add_customer'),
	url(r'^all_customers/',views.all_customers,name='all_customers'),
	url(r'^customer/(\d+)',views.single_customer,name='single_customer'),
	url(r'^search/', views.search_results, name='search_results'),
	url(r'^customer_location/(\d+)$',views.customer_in_location,name='customer_in_location'),
	url(r'^add_location/$', views.add_location, name='add_location')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

