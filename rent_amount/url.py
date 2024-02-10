from django.conf.urls import url
from rent_amount import views

urlpatterns = [
    url('add_rent_amount/(?P<idd>\w+)',views.add_rent_amount_render),
    url('view_rend_amont_admin/',views.view_rent_amount_admin),
    url('viw_rend_amnt_user/',views.view_rent_amount_user),
]