from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^login$', views.login),

    url(r'^process$', views.process),

    url(r'^register$', views.register),

    url(r'^cart$', views.cart),

    url(r'^dashboard$', views.dashboard),

    url(r'^review$', views.review),

    url(r'^showroom$', views.showroom),

    # url(r'^product$', views.product),

    # url(r'^edit$', views.edit),
#
    # url(r'^add$', views.add),


]
