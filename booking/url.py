from django.conf.urls import url
from booking import views
urlpatterns=[
    url('book_cycle/(?P<idd>\w+)',views.book_cycle),
    url('manage_bookind_render/',views.manage_booking_render),
    url('view_booking_status_user/',views.view_booking_status),
    url('accept/(?P<idd>\w+)', views.approve),
    url('reject/(?P<idd>\w+)', views.reject),

]