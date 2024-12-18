# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

from pyspark.sql.functions import col, concat_ws

# COMMAND ----------

cust_df=spark.read.csv(
    f'{bronze_path}/{customers_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

cust_df=cust_df.withColumn('FullName',concat_ws(' ',col('prefix'),col('FirstName'),col('LastName')))

# COMMAND ----------

cust_df=cust_df.drop('prefix','FirstName','LastName')

# COMMAND ----------

cust_df.write.mode('overwrite').parquet(f'{silver_path}/{customers_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")