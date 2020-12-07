# DAAR Project 3: CV Catcher

![Alt text](django_app/static/logo/logo_text.png?raw=true "CV Catcher")

Indexing CVs (PDF, Word, PNG and JPEG) in Elasticsearch and enabling search feature.

* [Introduction](#Introduction)

    * [Features](#Features)
    * [Quick Links](#Quick-Links)
    * [Search Queries](#Quick-Links)
        * [Examples](#Examples)
    * [DataSet](#dataset)

* [Getting started](#getting-started) (Instructions to build and run the project)
    * [Requirements](#requirements)
    * [Configure](#configure)
    * [build](#build)
    * [Run](#run)
    * [Test](#test)
* [Elasticsearch](#elasticsearch)
    * [Synchronization with the Database](#synchronization-with-the-database)
    * [Re-building the index](#re-building-the-index)
    * [Related Code](#related-code)
* [User Interfaces](#user-interfaces)

## Introduction

CV Catcher is a platform that enable people to share their CVs with Companies, and help companies to find quickly the
perfect candidate by enabling search feature over millions of CVs in different formats (PDF, Word, PNG, JPEG, ...).

### Features

- Admin Panel to manage CVs.
- Index and Search CVs (formats: PDF, Docx, PNG, JPEG, ...) throw the Admin Panel.
- UI for candidates to upload their CV without log-in.
- REST APIs that can be used with other clients.

### Quick Links

These are a shortcuts to help you access the Application quickly.

- [Admin Panel](http://localhost:8000/admin/cv/resume/) (username: admin, password: admin)
- [Upload CV Page](http://localhost:8000/)
- [REST APIs (Swagger Docs)](http://localhost:8000/api/swagger/)
- [REST APIs](http://localhost:8000/api/)

### Search Queries

We can perform a search with a list of keywords, and we can use the operators ```AND``` and ```OR```:

- to use ```AND``` we separate the keywords by a comma ```,```.
- to use ```OR``` we separate the keywords by a whitespace ``` ```.

#### Examples

- Example 00 (Simple Example):
  Candidates who speak Arabic
  ```
  Arabic
  ```

- Example 01 (```AND``` Operator):
  Candidates who code in JAVA AND Speak Arabic
  ```
  JAVA, Arabic
  ```

- Example 02 (```OR``` Operator):
  Candidates who code in JAVA OR C++
  ```
  JAVA C++
  ```
- Example 03 (```AND``` and ```OR```):
  Candidates who code in JAVA AND speak Arabic or English
  ```
  JAVA, Arabic English
  ```

### DataSet

The pre-loaded dataset contains 13 CVs with different formats (PDF, Word, PNG, JPG).

## Getting started

These instructions will get you a copy of the project up and running on your local machine or in a production server.
(Start by )

### Requirements

To make the system independent of the environment and make it easier for you to run it, we are using Docker.

1. [Docker or Docker Desktop](https://www.docker.com) (Docker engine 19+ with Docker compose).

### Configure

After cloning the repository, we start by configuring the environment:

1. Rename ```.env_example``` to ```.env``` or create an ```.env``` file in the root folder (same folder as ```docker-compose.yaml``` file) and copy the content of ```.env_example``` to ```.env``` file.
1. Optionally Customize the variables according to your preferences.

### Build

1. We start by building the images using the command
    ```shell script
    docker-compose build
    ```
1. Run the project
    ```shell script
    docker-compose up
    ```
1. Open a new tab in the terminal and run the migrations using the command
    ```shell script
    docker-compose run web python manage.py migrate
    ```
1. then create the index in ElasticSearch using the command
    ```shell script
    yes y | docker-compose run web python manage.py search_index --rebuild
    ```
1. Load the dataset (for the demo)
    ```shell script
    cat ./django_app/fixtures/backup.json | docker-compose run web python manage.py loaddata --format=json -
    ```

### Run

- To run the system
    ```shell script
    docker-compose up
    ```
- To shut down the system (from another tab)
    ```shell script
    docker-compose down
    ```

### Test

Run the system ```docker-compose up``` then

- To run the Unit Test
    ```shell script
    docker-compose run web python manage.py test apps
    ```

- To run the Unit Test with Coverage
    ```shell script
    docker-compose run web coverage run --source='./' manage.py test apps
    docker-compose run web coverage report
    ```

## Docker Architecture

The application consists of 3 containers:

1. *db* where the PostgreSQL instance is running.
1. *elasticsearch* where the ElasticSearch instance is running.
1. *web* where the backend server is running.

> ElasticSearch will persist data on ```./elasticsearch_data/``` folder (mounted-host volume).

> db (postgreSQL) will persist data on ```./postgres_data/``` folder (mounted-host volume).

## Elasticsearch

To use ElasticSearch with Django we are using the
package [https://github.com/django-es/django-elasticsearch-dsl](django-elasticsearch-dsl).

### Synchronization with the Database

To synchronize the PostgreSQL database with ElasticSearch, we are using Django signals
(events sent every time we Create, Update, Delete a model instance), and according to the received event we sync
ElasticSearch.

Once the event received we parse the CV file (PDF, Word or Image) to text, then we index it in ElasticSearch.

### Re-building the index

We provide also a command that will delete the index and re-create it, then re-build it for the whole database (all
existing CVs).

```bash
yes y | docker-compose run web python manage.py search_index --rebuild
```

### Related Code

Code related to ElasticSearch can be found at:

- Configuration ```./django_app/CV_CATCHER/settings.py```
- Indexing ```./django_app/apps/cv/documents.py```
- Search ```./django_app/apps/cv/admin.py``` and ```./django_app/apps/cv/views.py```

## User Interfaces

We can upload the CV throw the index page, or throw the Admin Panel

![Alt text](UIs/upload_cv.png?raw=true "Upload CV")

![Alt text](UIs/admin_upload_cv.png?raw=true "Admin Upload CV")

![Alt text](UIs/search.png?raw=true "Search")

![Alt text](UIs/search_res.png?raw=true "Search")

## About

Developed by students at Sorbonne University, just for learning purposes (part of DAAR lectures). Using Python with
Django, ElasticSearch and Docker.