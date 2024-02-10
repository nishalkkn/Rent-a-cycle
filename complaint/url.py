from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('send_complaint/',views.send_complaint),
    url('send_reply/(?P<idd>\w+)',views.send_reply_render),
    url('view_comp_admin/',views.view_complaints_admin),
    url('vew_cmp_render/',views.view_complaints_render),
    url('viw_reply_usr/',views.view_reply_user),

]