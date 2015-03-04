Direct Certificate Download and Discovery RESTFul Webservice
=================================================================

This document describes how to use the Direct Certificate Discovery API.
Django-direct has is now just a Django app that can be added to any 
Django project.
The following instructions illustrate running on the 
default Django development server 127.0.0.1:8000.


Certificate Fetching
====================

This tool downloads the certificate itself to your web client.


Format:


      http://127.0.0.1:8000/direct/get-certificate/[ENDPOINT]
    


Example 1 - Get the Certificate as ASCII Text
---------------------------------------------

To get the x509 Certificate if it exists:

    http://127.0.0.1:8000/direct/get-certificate/bill@hit-testing.nist.gov

Output:

    -----BEGIN CERTIFICATE-----
    MIIEJTCCAw2gAwIBAgIBBjANBgkqhkiG9w0BAQsFADBsMQswCQYDVQQGEwJVUzELMAkGA1UECAwC
    TUQxFTATBgNVBAcMDEdhaXRoZXJzYnVyZzENMAsGA1UECgwETklTVDERMA8GA1UEAwwIbmlzdC5n
    b3YxFzAVBgkqhkiG9w0BCQEWCG5pc3QuZ292MB4XDTE0MDQwMjE0MDEyOFoXDTE2MDQwMTE0MDEy
    OFowgYQxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJNRDEVMBMGA1UEBwwMR2FpdGhlcnNidXJnMQ0w
    CwYDVQQKDAROSVNUMR0wGwYDVQQDDBRoaXQtdGVzdGluZy5uaXN0LmdvdjEjMCEGCSqGSIb3DQEJ
    ARYUaGl0LXRlc3RpbmcubmlzdC5nb3YwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQ
    2Dhq3mH3zkl+8gmELWdVA5ZpPoSS0dyl0RuBt+UceP3w2fQHHOkSj92ZGjpSMWbrXtlsFa2daVGZ
    2EDjv5EpDTw55U7rSuD1S7scpmsYL7w3RhfFfhF2KLc63Z3v7EaVhp3Bora7kMJMSIlPrvIuQFTA
    zBy7Lbal9PiMPOuiPdrcon5OMDg7JOVBFyzq1bq0pm82q2PPPoXymHLXKfsBT0jjNtnKSFSJe12n
    2ibYqgk+T7XaRjaBCDyMkKfAkRI348zhFW7BgRnIUW+2hePQTleAYzci/AGSpbKrt5Ary9PDYCBC
    WHvbQdi9Cv7BGSCF+4xWPS9X9b9dE/wKX43RAgMBAAGjgbgwgbUwCQYDVR0TBAIwADAfBgNVHREE
    GDAWghRoaXQtdGVzdGluZy5uaXN0LmdvdjAdBgNVHQ4EFgQUi2D+g5UA4HxZB+1WQ3TKhE26cEUw
    HwYDVR0jBBgwFoAU2b5OviFqiWCvpYQPeeWHf/+8RF0wCwYDVR0PBAQDAgWgMDoGA1UdHwQzMDEw
    L6AtoCuGKWh0dHA6Ly9zYW1wbGVjYS5uaXN0Lmdvdi9jcmwvbmlzdC5nb3YuY3JsMA0GCSqGSIb3
    DQEBCwUAA4IBAQC1kG1vB0xMasYozmduZiqmM2lqYtXKw5t9pIBB+VqAweg7d29gQMF2/5c6ZKRZ
    FGdcWY04EOYIM88qitqEfgebe4eEX2NmyGreCJL/RH7Cl0ex5vbospL0uCO4NulRg/hFoOKOEkFD
    bL33Zj57kRvjK5WcvmtQe1rO/QuV5+n1+MGjy2+BPzPqXNqZRz8N8XSkKfLf0K3OlLHSItgCrvWo
    5JXGI0AZRVF4qxb6qgkywpRGu8LRs5qKQyzpJ91vZiLr/5ARhPsEKImEXb4VQqD8UgkeSxUHnyQV
    GneC5c7K3HW1/GmvYwTybLeDM+mnDzKD/6Nb2qXTUffHoTWtHF8M
    -----END CERTIFICATE-----



Example 2 - No Certificate Found
--------------------------------

If it doesn't exist, then you'll get an error message.  For example:


    http://127.0.0.1:8000/direct/get-certificate/foo@example.com

Output:
 

    No certificate was found via LDAP or DNS.
    


Example 3 - Get the Certificate as a .pem File
----------------------------------------------

Just add ".pem" to then end of the endpoint to get a PEM file instead of text.


    http://127.0.0.1:8000/direct/get-certificate/bill@hit-testing.nist.gov.pem


This will download a pem file with content_type="application/x-pem-file".


Certificate Validation
======================

This URL returns a JSON document containing information on whether or not the certificate 
was found and wheather it was found in DNS or LDAP. 

Format:


    http://127.0.0.1:8000/direct/validate/[ENDPOINT]
    

Example 4: A certificate was found in LDAP
------------------------------------------

Search for the certificate for the endpoint "domain2.demo.direct-test.com"


    http://127.0.0.1:8000/direct/validate/domain2.demo.direct-test.com

Output:


    {
    is_found: true,
    dns: {
         status: 404,
         message: "No Answer.",
         is_found: false,
         details: "The server did not provide an answer. No certificate found."
         },
     ldap: {
           status: 200,
           message: "The certificate domain2.demo.direct-test.com was found.",
           is_found: true
           }
    }


Example 5: No certificate was found
------------------------------------

Search for the certificate for the endpoint "foo@example.com".


    http://127.0.0.1:8000/direct/validate/foo@example.com

Output:


    {
    is_found: false,
    dns: {
         status: 404,
         details: "No DNS server found.",
         message: "Certificate not found.",
         is_found: false
         },
    ldap: {
          status: 404,
          details: "No LDAP server was found.",
          message: "No certificate found.",
          is_found: false
          }
    }
