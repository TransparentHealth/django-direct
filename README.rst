==============================================================
django-direct - A RESTFul API for Direct Certificate Discovery
==============================================================

django-direct is a simple Django application that provides a RESTFul 
API to validate and fetch Direct x509 certificate via LDAP and DNS.

Detailed documentation for using the API is in the "docs" directory. 
Installation instructions are below.

Quick start
-----------

1. Pip install django-direct::

    pip install django-direct


2. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'direct',
    )

3. Include the polls URLconf in your project urls.py like this::

    url(r'^direct/', include('direct.urls')),

4. There are no models in this application so there is no migration step.

5. Use the APIs.  Visit http://127.0.0.1:8000/direct/validate/[endpoint] to get a JSON validation report.
Visit http://127.0.0.1:8000/direct/get-certificate/[endpoint].pem to get a PEM certificate.
Visit http://127.0.0.1:8000/direct/get-certificate/[endpoint].txt to get the response as text repsonse. See docs folder for more information.

