from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ParquetSummary")
    .master("spark://bd-spark-master:7077")
    .getOrCreate()
)

import os

data_dir = "/opt/data" if os.path.exists("/opt/data") else "/home/jupyter/data"
input_path = f"{data_dir}/input/sample.parquet"
output_path = f"{data_dir}/output/sample.parquet"

df = spark.read.parquet(input_path)
df.summary().write.mode("overwrite").parquet(output_path)
print(f"Wrote summary to {output_path}")

spark.stop()
