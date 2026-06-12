# ETL / ELT Pipeline

## Objective

Transform raw cybersecurity events into analytical datasets suitable for machine learning and visualization.

## Pipeline Stages

### Extract

Source:
Cybersecurity attack dataset.

Tasks:

* Dataset ingestion
* Schema validation
* Initial profiling

### Load (RAW Layer)

Store original data.

Benefits:

* Data lineage
* Auditability
* Reproducibility

### Transform

Operations:

* Missing value treatment
* Data cleaning
* Feature selection
* Label encoding
* Data normalization

Generated Features:

* Attack Type
* Severity Level
* Protocol
* Traffic Type
* Network Segment
* Mexico State
* Anomaly Score

### Load (CLEAN Layer)

Output:

* Clean Parquet datasets
* ML-ready datasets

## Benefits

* Improved query performance
* Reduced storage requirements
* Standardized analytical datasets

## Technologies

* Python
* Pandas
* Parquet
* Jupyter Notebook

## Notebooks

01_etl_analysis.ipynb
02_eda_analysis.ipynb
03_ml_analysis.ipynb
