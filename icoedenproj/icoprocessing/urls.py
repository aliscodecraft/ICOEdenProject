from django.conf.urls import url
from . import views

urlpatterns = [url(r'^icoform/$', views.process_ico_form1, name='process_ico_form1')]