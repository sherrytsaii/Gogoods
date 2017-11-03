"""gogoods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from market.views.views import demo, register
from market.views.view_getdata import *
from market.views.view_search import home, post
from market.views.view_member import stand, standDetail, newTrans, buyerTranslations, memberDetail, editMember
from market.views.view_manager import vendorMag, buyerMag, mainMag, sdvdMag

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/$', demo, name='demo'),
    url(r'^home/$', home, name='home'),
    # Get Data
    # url(r'^userdata/$', get_Userdata),
    # url(r'^standdata/$', get_Standsdata),
    # url(r'^atmdata/$', get_ATMdata),
    # url(r'^localdata/$', get_Localdata),
    # url(r'^parkingdata/$', get_Parkingdata),
    # url(r'^marketdata/$', get_Marketsdata),

    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/home/'}),
    url(r'^accounts/register/$', register, name='register'),

    url(r'^member/vendor/stands/$', stand, name='stand'),
    url(r'^member/vendor/stands/(?P<id>\d+)/$', standDetail, name='standDetail'),
    url(r'^member/vendor/stands/newtrans/(?P<id>\d+)/$', newTrans, name='newTrans'),
    url(r'^member/buyer/translations/$', buyerTranslations, name='buyerTranslations'),
    url(r'^member/memberdetail/$', memberDetail, name='memberDetail'),
    url(r'^member/editmember/$', editMember, name='editMember'),

    url(r'^search/markets/(?P<pk>\d+)/$', post),

    url(r'^manager/$', mainMag, name='mainMag'),
    url(r'^manager/vendor/$', vendorMag, name='vendorMag'),
    url(r'^manager/buyer/$', buyerMag, name='buyerMag'),
    url(r'^manager/vendor/(?P<id>\d+)/$', sdvdMag, name='sdvdMag'),
]
