# Mutual Fund Analytics Pipeline

## Project Overview

The Mutual Fund Analytics Pipeline is a data engineering and analytics project that collects, processes, and analyzes mutual fund data. The project fetches live Net Asset Value (NAV) data from public APIs, stores it in CSV format, performs data quality checks, and prepares the data for further analysis and dashboard visualization.

## Objectives

* Fetch live mutual fund NAV data using APIs
* Store and manage historical mutual fund data
* Perform data quality validation
* Build an ETL (Extract, Transform, Load) pipeline
* Generate insights from mutual fund performance
* Create dashboards for visualization

## Project Structure

```text
Mutual-Fund-Analytics/
│
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── reports/
├── sql/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* SQLAlchemy
* Matplotlib
* Plotly
* Jupyter Notebook
* Git & GitHub

## Data Source

Mutual Fund API (MFAPI)

Sample Scheme:

* SBI Bluechip Fund

## Features Implemented

### Day 1

* Project setup completed
* Folder structure created
* Python environment configured
* Live NAV data fetched through API
* CSV data storage implemented
* Data ingestion pipeline created
* Data quality validation completed

## Sample Dataset Information

| Metric         | Value                |
| -------------- | -------------------- |
| File Name      | sbi_bluechip_nav.csv |
| Rows           | 3105                 |
| Columns        | 2                    |
| Missing Values | 0                    |

## Future Enhancements

* Multiple mutual fund scheme support
* Automated ETL pipeline
* SQL database integration
* Performance analytics
* Power BI Dashboard
* Streamlit Dashboard
* Risk and return analysis

## Author

**Chaitanya Raut**

Aspiring Data Engineer | Python | SQL | Data Analytics
