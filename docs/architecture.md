# CyberShield Analytics Architecture

## Architecture Overview

CyberShield Analytics implements a Data Lakehouse architecture designed for cybersecurity analytics.

The architecture combines data engineering, machine learning, geospatial analytics, and visualization components.

## Layers

### RAW Layer

Purpose:
Store original cybersecurity datasets without modifications.

Characteristics:

* Immutable data
* Original records
* Source preservation

### CLEAN Layer

Purpose:
Store transformed and validated datasets.

Processes:

* Missing value handling
* Data normalization
* Feature preparation
* Label encoding

### Analytics Layer

Provides:

* Threat Intelligence
* Geo Intelligence
* Machine Learning
* Model Evaluation

### API Layer

REST services expose analytics information.

Main Endpoints:

* /analytics/executive-kpis
* /threat/overview
* /geo/attacks-by-state
* /geo/mexico-geojson
* /ml/metrics
* /ml/best-model
* /api/status

### Presentation Layer

Interactive dashboards built using:

* AdminLTE
* Bootstrap
* ApexCharts
* Leaflet

## Data Flow

Data Source
↓
RAW Layer
↓
ETL/ELT
↓
CLEAN Layer
↓
Feature Engineering
↓
Machine Learning
↓
API Services
↓
Dashboards

## Deployment

* Docker Containerization
* Flask Backend
* Local Development Environment
