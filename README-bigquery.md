# Cloudmesh Google BigQuery 

* Deepak Deopura
* Gregor von Laszewski

## Abstract
- Connect ot Google BigQuery data warehouse and use Cloudmesh commands to interact with data sets and tables
- Read /write data from Google big query

## Objective
Develop Cloudmesh commands to interact with Google BigQuery, a google provided cloud based datawarehouse solution

## Motivation

- Learn about various data warehouse solution provided by major cloud providers (AWS,Azure,Google)
- Learn to work with cloud base datawarehouse and interaction with datawarehouse from cloud or local machine
- Understand data flow from/to datawarehouse, cloud and local and programmatically interact with cloud hosted data warehouse

## Terminology

- What is data warehouse? 
Data warehouse is used to collect data from multiple source system including RDBMS, transaction system, files and  and process data for analytical and decision support system.
datawarehose is used for business reporting, historical data analysis, dashboarding for better decision support. 

- What is different to RDBMS?
RDBMS is relational database to support and record transaction.
Data warehouse purpose is to support analytics and reporting and does not need real time data. It is optimized for data querying.
data is collected from multiple sources and processed to have single point of truth of data.
Data model is mostly denormalized to have efficient query time.
Transaction database purpose is to to record data transaction and it is optimized for insert/update then querying data.
data model is highly normalized and data processing is real time. 

## Releated Technologies

Some of data warehouse solutions by major cloud providers

- AWS data warehouse solution is AWS Redshift
- Azure Synapse Analytics isn sql base data warehouse and analytics solution by Azure
- BigQuery by Goolge is cloud based solution for data warehouse

####Cloudbased datawareouse solution comparison
Data warehouse solution can be compared based on some of following parameters
* Ability to scale up or scale out without affecting data. So that data warehouse can be scale up for high load data job or scale out to support concurrent jobs
* Independent of storage and compute
* Type of supported data like structural, JSON, semi structured, unstructured
* SQL and other support for easiness to query data

## Technology

* Python 
: Python libraries are used to programmatically interact with cloud and cloud hosted data warehouse
* Google Big query
: Google big query is cloud hosted data warehouse and provide analytical capabilities    
* Cloudmesh
: Cloudmesh provide solution to interact with multiple clouds from single entry point.
* NIST REST API

## Installation and Setup

Bigquery commands are part of cloudmesh-google so installation and setup is same as we have for cloudmesh-google.

You can use pip to install cloudmesh-google.

### Install via pip

```bash
$ pip install cloudmesh-cmd5
$ pip install cloudmesh-sys
$ pip install cloudmesh-cloud
$ pip install cloudmesh-google
```

### Installing from Source

```bash
$ git clone https://github.com/cloudmesh/cloudmesh-google.git
$ cd cloudmesh-google
$ pip install -e .
```

### Google Account creation and configuration

To create an google cloud account refer to [this page](https://cloudmesh.github.io/cloudmesh-manual/accounts/google/index.html) from the manual 

To configure Cloudmesh for the Google cloud account, here are the keys to edit.
Configuration via "~/.cloudmesh/cloudmesh.yaml"
* cloudmesh.cloud.google.credentials.project
* cloudmesh.cloud.google.credentials.json_file
* cloudmesh.cloud.google.credentials.datacenter

### Manual

Google big query commands have been created using Cloudmesh and Python libraries to programmatically interact with BigQuery.
    
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
## use case

Some of use cases of cloud based data warehouse
* Use cloud scale up to run heavy data load job 
* Use scale out to support multiple queries from user for better performance
* Able to programmatically control data warehouse based on job size and load on system
* Able to run queries and ML models on same dataset on different clouds

##Reference
*https://docs.microsoft.com/en-us/azure/sql-data-warehouse/*
*https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html*
*https://cloud.google.com/BigQuery/docs/*
