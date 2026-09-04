from pyspark.sql import SparkSession
import pandas as pd
spark=SparkSession.builder.appName("covid").getOrCreate()
csv_path="covid.csv"

spark_df=spark.read.csv(csv_path,header=True)
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