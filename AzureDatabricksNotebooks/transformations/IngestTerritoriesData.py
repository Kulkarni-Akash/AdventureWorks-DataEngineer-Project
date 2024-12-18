# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

ter_df=spark.read.csv(
    f'{bronze_path}/{territories_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

ter_df.write.mode('overwrite').parquet(f'{silver_path}/{territories_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")