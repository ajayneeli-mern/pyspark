from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ParquetSummary")
    .master("spark://bd-spark-master:7077")
    .getOrCreate()
)

input_path = "/opt/data/input/sample.parquet"
output_path = "/opt/data/output/sample_parquet_summary"

df = spark.read.parquet(input_path)
df.summary().write.mode("overwrite").parquet(output_path)
print(f"Wrote summary to {output_path}")

spark.stop()
