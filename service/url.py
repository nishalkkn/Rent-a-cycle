from django.conf.urls import url
from service import views

urlpatterns = [
    url('add_service/',views.add_service),
    url('view_service_public/',views.view_service_public),
    url('viw_servic_user/',views.view_service_user),
    url('vieew_svic_admin/', views.viw_service_admin),

]