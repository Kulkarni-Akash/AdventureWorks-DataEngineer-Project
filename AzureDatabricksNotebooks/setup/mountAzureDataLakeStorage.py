# Databricks notebook source
storageAccountName='adventureworkssa01'
client_id=dbutils.secrets.get(scope="AdventureWorksScope", key="client-id")
tenant_id=dbutils.secrets.get(scope="AdventureWorksScope", key="tenant-id")
client_secret=dbutils.secrets.get(scope="AdventureWorksScope", key="client-sceret")

# COMMAND ----------

configs={
    "fs.azure.account.auth.type":"OAuth",
    "fs.azure.account.oauth.provider.type":"org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id":client_id,
    "fs.azure.account.oauth2.client.secret":client_secret,
    "fs.azure.account.oauth2.client.endpoint":f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
}

# COMMAND ----------

def mountADLS(containerName):
    dbutils.fs.mount(
        source=f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/",
        mount_point=f"/mnt/{storageAccountName}/{containerName}",
        extra_configs=configs
    )

# COMMAND ----------

mountADLS("bronze")

# COMMAND ----------

mountADLS("silver")