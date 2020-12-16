from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^register/$',views.registerPage,name = 'register'),
    url('^login/$',views.loginPage,name = 'login'),
    url('^logout/$',views.logoutPage,name = 'logout'),

    url('^$',views.welcome,name = 'welcome'),

    url('^products/$',views.store,name = 'products'),
    url('^cart/$',views.cart,name = 'cart'),
    url('^checkout/$', views.checkout, name='checkout'),

    # url('^oneProduct/(\d+)/$',views.cart,name = 'oneProduct'),
	# url('^checkout/(\d+)/$', views.checkout, name='checkout'),
    
	url('^update_item/$',views.updateItem,name = 'update_item'),
	url('^process_order/$',views.processOrder,name = 'process_order'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)