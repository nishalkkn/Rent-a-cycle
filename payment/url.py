from django.conf.urls import url
from payment import views

urlpatterns = [
    url('send_payment/(?P<idd>\w+)',views.send_payment),
    url('view_payment_render/',views.view_payment_render),
    ]