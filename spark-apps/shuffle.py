from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ShuffleAndSkewDemo") \
    .master("spark://bd-spark-master:7077") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Create data with intentional skew
data = []

# Large number of records with same key = "HOT"
for i in range(900000):
    data.append(("HOT", i))

# Smaller keys
for key in range(1000):
    for i in range(100):
        data.append((f"key_{key}", key))


df = spark.createDataFrame(data, ["key", "value"])

print("Total Records:", df.count())

# Repartition to create multiple partitions
df = df.repartition(10, "key")

# GROUP BY creates SHUFFLE
result = df.groupBy("key") \
    .count()

# Trigger execution
result.show()

# Keep Spark UI alive
input("Press ENTER to stop Spark...")

spark.stop()