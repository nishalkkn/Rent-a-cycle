from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('add_feedback/',views.add_feedback),
    url('view_feedbck_admin/',views.view_feedback_admin),
    url('vew_fedbck_public/',views.view_feedback_public),
    url('viw_feeedbaack_render/',views.view_feedback_render),
]