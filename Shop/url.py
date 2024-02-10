from django.conf.urls import url
from Shop import views

urlpatterns = [
    url('shop_register/',views.shop),
]