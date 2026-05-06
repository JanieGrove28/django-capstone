# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# Add project root directory to Python path
sys.path.insert(0, os.path.abspath('../..'))

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

# -- Project information -----------------------------------------------------

project = 'django-capstone'
copyright = '2026, Janie Grové'
author = 'Janie Grové'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
