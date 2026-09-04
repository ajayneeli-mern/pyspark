from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SparkClusterSmokeTest")
    .master("spark://bd-spark-master:7077")
    .getOrCreate()
)

print(f"Spark version: {spark.version}")
print(f"Record count: {spark.range(1_000_000).count()}")

spark.stop()
