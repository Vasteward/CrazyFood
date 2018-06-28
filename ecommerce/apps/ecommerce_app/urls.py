from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^login$', views.login),

    url(r'^cart$', views.cart),

    url(r'^dashboard$', views.dashboard),

    url(r'^borrower$', views.borrower),
]
