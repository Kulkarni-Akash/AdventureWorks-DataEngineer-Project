# AdventureWorks-DataEngineer-Project

## Overview
AdventureWorks is a data engineering project that uses Azure services to demonstrate the end-to-end data pipeline process. The project is based on the AdventureWorks dataset and focuses on data extraction, transformation, and loading (ETL) workflows.

## Architecture Diagram
The following architecture diagram illustrates the flow of data across different Azure services used in this project:

![AdventureWorksProject Architecture](https://github.com/user-attachments/assets/afbdb0e1-3d0a-450b-a9b4-55e9e1863d47)

## Project Objectives
- Extract data from GitHub using Azure Data Factory (ADF).
- Perform data cleaning and transformation using Azure Databricks.
- Store data in Azure Data Lake Storage (ADLS) with a structured approach:
  - **Bronze Container**: Stores raw data.
  - **Silver Container**: Stores transformed and cleaned data for analysis.
 
## Technologies Used
- **Azure Data Factory (ADF)**: For data extraction and orchestration.
- **Azure Databricks**: For data cleaning, transformation, and processing using PySpark.
- **Azure Data Lake Storage (ADLS)**: For scalable and secure data storage.
- **Azure Key Vault**: For storing the credentials/passwords securely without exposing them.
- **GitHub**: Source of raw data for the project.

## Data Pipeline Workflow
1. **Data Extraction**:
   - ADF pipelines were used to fetch raw data directly from the GitHub repository.
   - **Snapshot of the ADF Pipeline**:
     ![ADF pipeline](https://github.com/user-attachments/assets/192af36d-f4eb-4fdf-a8be-7b717b107e74)
2. **Data Cleaning and Transformation**:
   - Azure Databricks was employed to clean the data using PySpark.
   - Applied business rules and transformations to prepare the data for storage.
   - The Databricks notebook is provided in the repository under the `Databricks-Notebooks` folder.
3. **Data Storage**:
   - Raw data was stored in the **Bronze Container** of ADLS.
   - Cleaned and transformed data was stored in the **Silver Container** of ADLS for downstream use.

## Key Features
- End-to-end orchestration of data pipelines using Azure Data Factory.
- Scalable and distributed data processing with Azure Databricks.
- Organized and tiered storage structure in Azure Data Lake Storage.

## Source Data
The raw data for this project is sourced from Kaggle, access the dataset here: [AdventureWorks](https://www.kaggle.com/datasets/ukveteran/adventure-works)
