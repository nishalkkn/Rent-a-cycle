from django.conf.urls import url
from distance_tracking import views

urlpatterns = [
    url('add_dis_travelled_usr/',views.add_distance_travelled),
    url('view_dist_trvled_render/',views.view_distance_travelled_render),
]