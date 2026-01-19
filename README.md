# healthcare-analytics-etl
# Healthcare Analytics ETL Pipeline

## Overview
This project implements an end-to-end ETL pipeline that transforms raw healthcare
visit data into analytics-ready datasets for reporting and operational insights.

The pipeline extracts raw encounter-level data, applies data cleaning and validation,
engineers analytical features, and loads the results into a SQL database for analysis.

This project is designed to mirror real-world analytics engineering workflows, emphasizing data quality, schema consistency, and analytical usability.


## Project Highlights
- Built an end-to-end Python ETL pipeline for healthcare operational data
- Implemented data validation rules to ensure analytics-ready datasets
- Engineered visit duration and cost metrics for downstream analysis
- Designed SQL queries for utilization analysis and outlier detection

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
- Load cleaned data into a relational database (SQLite), with a design that is portable to cloud data warehouses
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

## Future Improvements
- Deploy the pipeline to a cloud data warehouse (e.g., Google BigQuery)
- Add automated pipeline orchestration
- Extend data quality checks with schema enforcement
- Support additional data sources

## How to Run the Pipeline

1. Extract raw data:
   ```bash
   python src/extract.py

2. Transform and clean the data:
   ```bash
   python src/transform.py

3. Load the cleaned data into the database:
   ```bash
   python src/load.py

4. Run analytical queries:
   - Open the SQLite database (healthcare.db)
   - Execute the SQL queries in sql/analytics.sql to analyze utilization, cost trends, and outliers
   
