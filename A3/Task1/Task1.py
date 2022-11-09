#!/usr/bin.env python3
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean

import sys
import shutil
import os

# Run command : spark-submit Task1.py "data/spark-5-percent-dataset.csv" "output"

# Create spark session
spark = SparkSession.builder.getOrCreate()

# Read input file passed as first arg
df = spark.read.csv(sys.argv[1],header=True,inferSchema=True)

# Drop all null valued rows
df = df.na.drop()

# Eliminate duplicate rows
df = df.dropDuplicates()

# Finding average of each state
avg = df.groupby('RP State Plate').avg('Fine amount')
avg.filter(avg['RP State Plate'] == 'WA').show()

# Query conditions
res_1 = df.filter(df["Color"] == "WH")
res_join = res_1.join(avg,res_1["RP State Plate"] == avg["RP State Plate"], "inner")
res = res_join.filter(res_join["Fine amount"] > res_join["avg(Fine amount)"])
res.filter(res["Ticket number"] == 1109149683).show()

# Sort shuffled data
res = res.sort("Ticket number")

# Select only the ticket number column
res = res.select("Ticket number")

# Delete ouput folder if it already exists
if os.path.exists(sys.argv[2]):
    shutil.rmtree(sys.argv[2])

# Write to output folder
res.coalesce(1).write.csv(sys.argv[2])