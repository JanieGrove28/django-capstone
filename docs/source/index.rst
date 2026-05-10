Django Capstone Documentation
=============================

Welcome to the Django Capstone project documentation.

Overview
--------

This project is a Django web application developed as part of a capstone project.

Features
--------

* Django web development
* Docker containerisation
* Sphinx documentation
* Git version control

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Docker
------

Build the Docker image:

.. code-block:: bash

   docker build -t django-capstone .

Run the Docker container:

.. code-block:: bash

   docker run -p 8000:8000 django-capstone
   