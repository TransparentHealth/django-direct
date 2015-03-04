from django.shortcuts import render
from django.http import HttpResponse
from getdc.getdc import validate_certificate, get_certificate
import json

def validate_direct_endpoint(request, endpoint):
    result = validate_certificate(endpoint)
    return HttpResponse(json.dumps(result),
                content_type="application/json")
    

def get_direct_endpoint_certificate(request, endpoint, file_extension="pem"):
    result = get_certificate(endpoint)    
    response = HttpResponse(result, content_type="text/plain; charset=us-ascii") 
    
    if request.path.endswith(".pem") and result.__contains__("-----BEGIN CERTIFICATE-----"):
        response = HttpResponse(result, content_type="application/x-pem-file") 
    return response


