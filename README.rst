==========
Direct API
==========

Direct is a simple Django app that provides a RESTFul 
API to validate and fetch Direct certificate.

Detailed documentation is in the "docs" directory.

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

5. Use the APIs. Visit http://127.0.0.1:8000/direct/validate/[endpoint] to get a JSON validation report.
Visit http://127.0.0.1:8000/direct/get-certificate/[endpoint].pem to get a PEM certificate.
Visit http://127.0.0.1:8000/direct/get-certificate/[endpoint].txt to get the response as text repsonse.

