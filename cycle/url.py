from django.conf.urls import url
from cycle import views

urlpatterns = [
    url('add_cycle/',views.cycle),
    url('view_cycle_admin/',views.view_cycle_admin),
    url('vew_ccle_public/',views.view_cycle_public),
    url('viw_cycle_user/',views.view_cycle_user),

]