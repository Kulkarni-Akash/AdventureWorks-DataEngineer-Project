# Databricks notebook source
# MAGIC %run ./config/config

# COMMAND ----------

for i in notebookNames:
    dbutils.notebook.run(f'{folderPath}/{i}',0)