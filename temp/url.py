from django.conf.urls import url
from temp import views

urlpatterns = [
    url('admin/',views.admin),
    url('public/', views.public),
    url('shop/', views.shop),
    url('user/', views.user),
    url('home_usr/', views.home_usr),
    url('he_shop/', views.home_shop),
    url('hm_admin/', views.home_admin),
    url('hme_public/', views.home_public),

]