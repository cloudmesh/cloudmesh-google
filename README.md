# Cloudmesh Google Providers

[![image](https://img.shields.io/travis/TankerHQ/cloudmesh-google.svg?branch=main)](https://travis-ci.org/TankerHQ/cloudmesh-google)

[![image](https://img.shields.io/pypi/pyversions/cloudmesh-google.svg)](https://pypi.org/project/cloudmesh-google)

[![image](https://img.shields.io/pypi/v/cloudmesh-google.svg)](https://pypi.org/project/cloudmesh-google/)

[![image](https://img.shields.io/github/license/TankerHQ/python-cloudmesh-google.svg)](https://github.com/TankerHQ/python-cloudmesh-google/blob/main/LICENSE)

see cloudmesh.google

* https://github.com/cloudmesh/cloudmesh-google

## Introduction
Cloudmesh-google provider offers various cloud engineering operations via command line.
cloudmesh-google storage module provides following options via command line using `cms storage`  :
* create dir
* put
* get
* list
* delete

Also following options are available via command line using `cms google` :
* json_to_yaml (adds json file information to yaml)
* yaml_to_json (creates a json file from yaml entry)
* list_bucket
* create_bucket
* blob_metadata
* rename_blob
* copy_blob_btw_buckets

cloudmesh-google compute module provides following options via command line using `cms com[pute`  :

* flavor 
* create IP
* delete IP
* list IP
* find available IP
* get IP

IP Reference: https://cloudmesh.github.io/cloudmesh-manual/manual/ip.html

Flavor Reference: https://cloudmesh.github.io/cloudmesh-manual/manual/flavor.html

## Installation
Refer installation of cloudmesh-google:
* https://cloudmesh.github.io/cloudmesh-manual/installation/index.html

## References

* Google account creation https://cloudmesh.github.io/cloudmesh-manual/accounts/google/account.html

## Specifications

* google-cloud-storage
* google-cloud-compute

### json

```
    {
      "type": "service_account",
      "project_id": "imposing-coast-257700",
      "private_key_id": "xxxxxxxx....",
      "private_key": "-----BEGIN PRIVATE KEY-----\nxxxxxxxxxx\n-----END PRIVATE KEY-----\n",
      "client_email": "user@imposing-coast-257700.iam.gserviceaccount.com",
      "client_id": "12345678...",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/" \
                              "user%40imposing-coast-257700.iam.gserviceaccount.com"
    }

```

### API Reference

Using API through Google API Python Client:  

```
from googleapiclient.discovery import build

compute = build('compute', 'v1', developerKey=apiToken) #Multiple API versions, I assume v1 is the one we want to use

instances = compute.instances() #Holds operations for working with specific instances
instances.list() #List available instances
instances.delete(project, zone, instance) # Delete specific instance
#Etc.
```

API reference: <http://googleapis.github.io/google-api-python-client/docs/dyn/compute_v1.html>

## Pytest

Test the IP's functions:

```
cms set cloud=google 
cd cloudmesh-google
pytest -v --capture=no tests/test_ip.py
pytest -v  tests/test_ip.py
```

for indivual test:

```
pytest -v --capture=no  tests/test_ip.py::TestIp::test_cms_ip_list
pytest -v --capture=no  tests/test_ip.py::TestIp::test_cms_create_ip
pytest -v --capture=no  tests/test_ip.py::TestIp::test_cms_delete_ip
```

Test the flavor

```
cms set cloud=google
cd cloudmesh-cloud
pytest -v --capture=no tests/cloud/test_04_flavor.py
```

for indivual test:

```
pytest -v --capture=no tests/cloud/test_04_flavor.py::Test_Flavor::test_empty_database
pytest -v --capture=no tests/cloud/test_04_flavor.py::Test_Flavor::test_provider_flavor
pytest -v --capture=no tests/cloud/test_04_flavor.py::Test_Flavor::test_provider_flavor_update
pytest -v --capture=no tests/cloud/test_04_flavor.py::Test_Flavor::test_cms_flavor_refresh
pytest -v --capture=no tests/cloud/test_04_flavor.py::Test_Flavor::test_cms_flavor
```