# healthcare-analytics-etl
# Healthcare Analytics ETL Pipeline

## Overview
This project implements an end-to-end ETL pipeline that transforms raw healthcare
visit data into analytics-ready datasets for reporting and operational insights.

The pipeline extracts raw encounter-level data, applies data cleaning and validation,
engineers analytical features, and loads the results into a SQL database for analysis.

## Data Source
Synthetic healthcare visit data representing patient encounters across departments,
including timestamps, costs, and diagnoses.

## Pipeline Architecture
**Extract**
- Load raw CSV data using Python (pandas)

**Transform**
- Standardize schema and data types
- Handle invalid and duplicate records
- Engineer visit duration metrics
- Enforce basic data quality rules

**Load**
- Load cleaned data into a relational database (SQLite)
- Prepare tables for analytical querying

**Analyze**
- SQL queries for utilization, cost trends, and outlier detection

## Data Quality Checks
- Removal of duplicate visit records
- Validation of non-negative costs
- Validation of visit duration logic
- Schema consistency checks

## Example Analytics
- Average visit duration by department
- Visit volume distribution
- Highest-cost encounters

## Tech Stack
- Python (pandas)
- SQL
- SQLite
- Git & GitHub

