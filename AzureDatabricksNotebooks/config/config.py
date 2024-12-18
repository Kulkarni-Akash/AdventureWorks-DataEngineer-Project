# Databricks notebook source
bronze_path='/mnt/adventureworkssa01/bronze'
silver_path='/mnt/adventureworkssa01/silver'

# COMMAND ----------

calendar_path='calendar'
customers_path='customers'
productCategories_path='productCategories'
products_path='products'
productSubCategories_path='productSubCategories'
returns_path='returns'
sales_path='sales'
territories_path='territories'

# COMMAND ----------

folderPath="/Workspace/Users/akazurelearning22@gmail.com/AdventureWorks/transformations"

# COMMAND ----------

notebookNames=[
    'IngestCalendarData',
    'IngestCustomersData',
    'IngestProductCategoriesData',
    'IngestProductsData',
    'IngestProductSubCategoriesData',
    'IngestReturnsData',
    'IngestSalesData',
    'IngestTerritoriesData'
]