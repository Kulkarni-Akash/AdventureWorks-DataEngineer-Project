# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

prdSubCat_df=spark.read.csv(
    f'{bronze_path}/{productSubCategories_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

prdSubCat_df.write.mode("overwrite").parquet(f'{silver_path}/{productSubCategories_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")