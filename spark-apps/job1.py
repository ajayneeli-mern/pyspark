from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("covid")
    .master("spark://bd-spark-master:7077")
    .getOrCreate()
)
print('###################')
print("Application name:", spark.sparkContext.appName)
print("Application ID:", spark.sparkContext.applicationId)
print("Spark UI:", spark.sparkContext.uiWebUrl)
print('###################')
csv_path = "/opt/data/input/covid.csv"

spark_df = spark.read.csv(csv_path, header=True)
#spark_df.show()

selected_df = spark_df.select(
    "continent",
    "country",
    "population",
    "`cases.new`",
    "`cases.active`",
    "`cases.critical`",
    "`cases.recovered`",
    "`tests.total`"
)

# Show the resulting DataFrame with the selected columns
selected_df.show()
# Display all rows without truncation
#selected_df.show(n=selected_df.count(), truncate=False)
# Fill null values with 0 for specific columns
df_filled = selected_df.fillna({'`cases.new`': 0, '`cases.active`': 0, '`cases.critical`': 0, '`cases.recovered`': 0, '`tests.total`': 0})
df_filled.show()

spark.stop()
