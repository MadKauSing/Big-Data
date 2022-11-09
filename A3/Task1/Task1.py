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

avg_amt = df.select(mean('Fine amount')).alias('avg').collect()[0].asDict()
df.show(10)
print(avg_amt['avg(Fine amount)'])

# Delete ouput folder if it already exists
if os.path.exists(sys.argv[2]):
    shutil.rmtree(sys.argv[2])
# Write to output folder
df.write.csv(sys.argv[2])