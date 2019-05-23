from django.conf.urls import url

from cb import views

urlpatterns = [
    url(r'^base/$', views.base, name='base'),  # 基准页

    url(r'^$', views.home, name='home'), # 默认首页

    url(r'^home/$', views.home, name='home'),

    url(r'^new_forms/$', views.new_form, name='new_forms')


]