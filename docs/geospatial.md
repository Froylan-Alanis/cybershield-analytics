# Geo Intelligence Module

## Objective

Provide geographical visualization of cybersecurity attacks across Mexico.

## Features

### Threat Map

Interactive map built with:

* Leaflet
* GeoJSON
* OpenStreetMap

### Attack Distribution by State

Displays:

* Total attacks per state
* Geographic concentration
* Regional comparison

### Interactive Visualization

Capabilities:

* Hover effects
* State highlighting
* Popup information
* Dynamic coloring

## Data Sources

### GeoJSON

Mexico administrative boundaries.

Location:

data/geojson/

### Analytics Data

Endpoint:

/geo/attacks-by-state

## Workflow

Attack Dataset
↓
State Aggregation
↓
API Endpoint
↓
GeoJSON Join
↓
Leaflet Rendering
↓
Interactive Threat Map

## Benefits

* Spatial threat analysis
* Regional attack identification
* Geographical intelligence support
