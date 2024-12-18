# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

ret_df=spark.read.csv(
    f'{bronze_path}/{returns_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

ret_df.write.mode("overwrite").parquet(f'{silver_path}/{returns_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")