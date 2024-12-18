# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

prd_df=spark.read.csv(
    f'{bronze_path}/{products_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

prd_df.write.mode('overwrite').parquet(f'{silver_path}/{products_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")