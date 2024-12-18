# Databricks notebook source
# MAGIC %run ../config/config

# COMMAND ----------

from pyspark.sql.functions import col, month, year

# COMMAND ----------

cust_df=spark.read.csv(
    f'{bronze_path}/{calendar_path}',
    header=True,
    inferSchema=True
)

# COMMAND ----------

cust_df=cust_df.withColumn("Month",month(col("Date"))) \
    .withColumn("Year",year(col("Date")))

# COMMAND ----------

cust_df.write.mode('overwrite').parquet(f'{silver_path}/{calendar_path}')

# COMMAND ----------

dbutils.notebook.exit("Success")