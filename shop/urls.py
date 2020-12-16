from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^register/$',views.registerPage,name = 'register'),
    url('^login/$',views.loginPage,name = 'login'),
    url('^logout/$',views.logoutPage,name = 'logout'),


    url('^$',views.welcome,name = 'welcome'),
    url('^category/(\d+)/$',views.list_category,name = 'category'),
    url('^products$',views.display_product,name = 'products'),
    url('^oneProduct/(\d+)/$',views.single_product,name = 'oneProduct'),
    
    url('^store/$', views.store, name='store'),
	url('^cart/$', views.cart, name='cart'),
	url('^checkout/$', views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)