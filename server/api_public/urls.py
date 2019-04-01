from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^api/get-products/$', views.product_list),
    url(r'^api/get-product/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^api/lists-and-products/$', views.add_products_to_lists.as_view()),
    url(r'^api/create_list/$', views.create_list.as_view()),
    url(r'^api/list/(?P<pk>[0-9]+)$', views.list.as_view()),
    url(r'^api/lists/$', views.lists.as_view()),
    # url(r'^transactions/(?P<pk>[0-9]+)$', views.transaction_detail.as_view()),
]