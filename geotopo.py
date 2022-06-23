# Databricks notebook source
path = '/Workspace/Repos/rishabh.gaur@celebaltech.com/map/District.json'

# COMMAND ----------

file = open('District.json')

# COMMAND ----------

import os
os.getcwd()

# COMMAND ----------

file_geo = open("/FileStore/rishabh_gaur/geotest/1.geojson")

# COMMAND ----------

dbutils.fs.mv('dbfs:/FileStore/rishabh_gaur/geotest', '/Workspace/Repos/rishabh.gaur@celebaltech.com/map/Test/', recurse=True)

# COMMAND ----------

/Workspace/Repos/rishabh.gaur@celebaltech.com/map/Test/

# COMMAND ----------

# MAGIC %fs ls '/Workspace/Repos/rishabh.gaur@celebaltech.com/map/Test/'

# COMMAND ----------


