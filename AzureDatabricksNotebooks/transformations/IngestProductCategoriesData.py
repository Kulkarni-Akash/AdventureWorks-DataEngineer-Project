# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

prdCat_df=spark.read.csv(
    f'{bronze_path}/{productCategories_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

prdCat_df.write.mode('overwrite').parquet(f'{silver_path}/{productCategories_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")