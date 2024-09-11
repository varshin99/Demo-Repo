# Databricks notebook source
a=3
b=3
c=a+b
c

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "HELLO"
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #title 1
# MAGIC ##title 2
# MAGIC

# COMMAND ----------

# MAGIC %run ./includes/Setup

# COMMAND ----------

full_name

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls("/databricks-datasets")

# COMMAND ----------

display(files)

# COMMAND ----------


