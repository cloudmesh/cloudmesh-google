# Cloudmesh Google BigQuery 

* Deepak Deopura
* Gregor von Laszewski

## Abstract

* Connect ot Google BigQuery data warehouse and use Cloudmesh commands to interact with data sets and tables
* Read /write data from Google big query

## Objective

Develop 

1. Provide a survey and comparision of cloud providers and services that offer big query like features
2. Provide a Cloudmesh API that can be used to interact with multiple cloud providerd that offer big query like features.
1. Provide Cloudmesh command(s) to interact with multiple cloud providers that offer google big query like features.

Google BigQuery is a a google provided cloud based datawarehouse solution.

## Motivation

* Learn about various data warehouse solution provided by major cloud providers (AWS,Azure,Google)
* Learn to work with cloud base datawarehouse and interaction with datawarehouse from cloud or local machine
* Understand data flow from/to datawarehouse, cloud and local and programmatically interact with cloud hosted data warehouse

## Terminology

* What is data warehouse? 

Data warehouse is used to collect data from multiple source system including RDBMS, transaction system, files and  and process data for analytical and decision support system.
datawarehose is used for business reporting, historical data analysis, dashboarding for better decision support. 

* What is different to RDBMS?

RDBMS is relational database to support and record transaction.
Data warehouse purpose is to support analytics and reporting and does not need real time data. It is optimized for data querying.
data is collected from multiple sources and processed to have single point of truth of data.
Data model is mostly denormalized to have efficient query time.
Transaction database purpose is to to record data transaction and it is optimized for insert/update then querying data.
data model is highly normalized and data processing is real time. 

## Releated Technologies

Some of data warehouse solutions by major cloud providers

* AWS data warehouse solution is AWS Redshift (https://aws.amazon.com/redshift/)
* Azure Synapse Analytics isn sql base data warehouse and analytics solution by Azure (https://azure.microsoft.com/en-us/services/synapse-analytics/)
* BigQuery by Google is cloud based solution for data warehouse (https://cloud.google.com/bigquery)
* Snowflake by Snowflake computing based on SQL. Snowflake use other public cloud like AWS or GCP for their solution (https://www.snowflake.com/)

### Cloudbased datawareouse solution comparison

Data warehouse solution can be compared based on some of following parameters

* Ability to scale up or scale out without affecting data. So that data warehouse can be 
  scale up for high load data job or scale out to support concurrent jobs
* Independent of storage and compute
* Type of supported data like structural, JSON, semi structured, unstructured
* SQL and other support for easiness to query data

|                                  	| Big Query                                                                                	| AWS redshift                                                                                                           	| Snowflake                                                                                                                	|
|----------------------------------	|------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------	|
| Storage   and compute            	| Separate data storage,   processing and compute                                          	| Combined storage and compute                                                                                           	| separate compute and storage                                                                                             	|
| Scalability                      	| Automatic provision of compute   resource based o load.                                  	| Local scale. Can not be scaled   independently. Need to reconfigure cluster and restart it to scale.                   	| Separate metadata, compute and   storage. Compute and storage can be independently scaled   horizontally/vertically      	|
| Security                         	| Highly secure, encrypt all data   in rest or in transit                                  	| High security. Addition to DB   security, there is other security features like SSL connection, sign-in   credentials  	| Fair and as per industry   standards. Options of security is available and it impact on costing..                        	|
| SQl   capability                 	| ANSI 2011 SQL standards. Support   for XML and JSON. Can be improved for complex queries 	| Limited SQL capabilities for   example , it does not support constraints, index, partitions                            	| Support JSOn, XML, AVRO, Parquet   data types. Standard and extended sql support. Limited performance tunning   options. 	|
| Maintenance   and operationalize 	| Low maintenance, backend support   and configuration is handled by google.               	| Complex to integrate. Need   customer time for maintenance like    updates                                             	| Zero management from end   customer.                                                                                     	|


## Technology used for the implementation

* Python 
: Python libraries are used to programmatically interact with cloud and cloud hosted data warehouse
* Google Big query
: Google big query is cloud hosted data warehouse and provide analytical capabilities    
* Cloudmesh
: Cloudmesh provide solution to interact with multiple clouds from single entry point.
* NIST REST API

## Installation and Setup

```bash
$ pip install cloudmesh-installer
$ cloudmesh-installer install google
```

### Installing from Source

```bash
$ git clone https://github.com/cloudmesh/cloudmesh-google.git
$ cd cloudmesh-google
$ pip install -e .
```

### Google Account creation and configuration

To create an google cloud account refer to 
[this page](https://cloudmesh.github.io/cloudmesh-manual/accounts/google/index.html) from the manual 

To configure Cloudmesh for the Google cloud account, here are the keys to edit.
Configuration via `~/.cloudmesh/cloudmesh.yaml`

* cloudmesh.cloud.google.credentials.project - project name which has been created on google cloud (https://cloud.google.com/resource-manager/docs/creating-managing-projects) 
* cloudmesh.cloud.google.credentials.json_file - json file generated from google for authentication (https://cloud.google.com/docs/authentication/getting-started)
* cloudmesh.cloud.google.credentials.datacenter - Google region which is used to setup your account.


### Manual

Google big query commands have been created using Cloudmesh and Python libraries to programmatically interact with BigQuery.

```
        Usage:
                google bigquery list
                google bigquery listtables DATASET_ID
                google bigquery describetable DATASET_ID TABLE_ID


        Arguments:
            DATASET_ID              The Google BigQuery dataset id.
            PROJECT_ID              The google big query project id
            TABLE_NAME              The name of the table

        Description:
            google bigQuery list
                List all datasets present in given project_id

            google bigQuery listtables DATASET_ID
                List all tables from given dataset and project

            google bigQuery describetable DATASET_ID TABLE_ID
                Describe given TABLE_ID along with schema, row count, columns type.
```

## Usecase

Some of use cases of cloud based data warehouse

* Programmatically scale up or scale horizontal for better query performance
* Use scale out to support concurrent queries on datawarehouse to increase throughput
* Able to run queries and ML models on same dataset on different clouds provided solution

## References

* <https://docs.microsoft.com/en-us/azure/sql-data-warehouse/>
* <https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html>
* <https://cloud.google.com/BigQuery/docs/>
* <https://docs.snowflake.com/en/user-guide/intro-supported-features.html>
