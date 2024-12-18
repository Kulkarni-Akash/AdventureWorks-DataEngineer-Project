# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

from pyspark.sql.functions import col, year

# COMMAND ----------

sal_df=spark.read.csv(
    f'{bronze_path}/{sales_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

sal_df=sal_df.withColumn('OrderYear',year(col('OrderDate')))

# COMMAND ----------

sal_df.write.mode('overwrite').partitionBy('OrderYear').parquet(f'{silver_path}/{sales_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")