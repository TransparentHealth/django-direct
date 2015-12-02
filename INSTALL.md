Custom/Local  Install Instructions for Django-Direct API and Test Tool
======================================================================

This document outlines installing the software in Amazon web Service (AWS) 
Elastic Cloud Computing (EC2), but the information contained here is 
also mostly applicable to local installs. You won't need this if 
following these instructions, but the source code for this application 
can be found here. https://github.com/videntity/django-djmongo.

This Amazon Machine Image (AMI) is a pre-built image that 
will lanch django-direct in AWS EC2. The direct app is bound to "/" the root. 

It was created to streamline the setup of a separate 
personal installation and provide a full working example for 
those seeking to setup a local deployment.

The AMI is `ami-f532709f`.

You can use this URL to kick things off. 

https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-f532709f

A micro-instance is suitble for a low traffic installation.

Overview of Stack Components
-----------------------------

* Ubuntu Linux 14.04 64-bit Version
* Apache2 with mod_wsgi
* Python 2.7 / Django 1.8.3
* Bootstrap, JQuery, JavaScript
* sqlite3
* OpenSSL
* A number of Python and C libraries


After your instance is lanched EC2 will assign a hostname and IP.

After the instance is launched point your browser to

http://youhost.amazonaws.com replacing yourhost with your actual 
running instance's host name. You won't be able to see the console 
until DNS is configured.  See the first step below.

Your To Do Items To Complete and Customize the Installation:
============================================================



**NOTE**: This software is provided without any warranty under the 
terms of the GPL v2 license. Commercial licenses avaialable.

Setup DNS
---------

Setup DNS for your own needs as needed.

SSH Login
---------

This is not absolutley necessary, but you will need this for most any configuration change, to enable SSL, and to setup outbound email.

Login Example:


    ssh -i yourkey.pem ubuntu@yourhost.com

Credentials


* Username: `ubuntu`
* Password: `None`  (You'll use youe own EC2 certificates for access.) Use `sudo` or `sudo su -` for rootly commands.


Enable HTTPS/SSL
----------------

Only use this tool/API  using HTTPS. Enabling SSL will require obtaining 
certificates install onto the Apache webserver. This is well documented 
elswhere online. Here are a couple hints to get you going in the right 
direction:

 * Keep in mind, these certificates are separate from certificates generated from this application.
 * Here is a reasonable tutorial: https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-12-04
