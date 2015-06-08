#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from views import *
from  django.views.generic.base import TemplateView

urlpatterns = patterns('',

    
    #Direct
    url(r'^validate/(?P<endpoint>\S+)', validate_direct_endpoint,
        name="validate_direct_endpoint"),
    
    url(r'^get-certificate/(?P<endpoint>\S+).pem',
        get_direct_endpoint_certificate,
        name="get_direct_endpoint_certificate_pem"),
    
    url(r'^get-certificate/(?P<endpoint>\S+).txt',
        get_direct_endpoint_certificate,
        name="get_direct_endpoint_certificate_text"),
    
    url(r'^get-certificate/(?P<endpoint>\S+)',
        get_direct_endpoint_certificate,
        name="get_direct_endpoint_certificate_no_extension"),
    
    url(r'^$', TemplateView.as_view(template_name='direct/splash.html'),
        name="direct_splash"),

    )
