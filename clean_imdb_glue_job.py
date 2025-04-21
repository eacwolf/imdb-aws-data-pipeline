from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, trim, when
from pyspark.sql.types import IntegerType, FloatType
import pyspark.sql.functions as F

# Initialize Spark
spark = SparkSession.builder.appName("IMDB_Cleaning").getOrCreate()

# Load data
df = spark.read.option("header", True).csv("s3://akhil-pipeline/imdb_top_1000_csv/imdb_top_1000.csv")

#  Drop the Poster_Link column
df = df.drop("Poster_Link")

# Clean 'Gross' column: remove commas and convert to float
df = df.withColumn("Gross", regexp_replace("Gross", ",", ""))
df = df.withColumn("Gross", col("Gross").cast(FloatType()))

#  Calculate median of Gross
median_val = df.approxQuantile("Gross", [0.5], 0.0)[0]

# Fill missing Gross with median
df = df.withColumn("Gross", when(col("Gross").isNull(), median_val).otherwise(col("Gross")))

# Clean 'Runtime': remove ' min' and convert to integer
df = df.withColumn("Runtime", regexp_replace("Runtime", " min", ""))
df = df.withColumn("Runtime", col("Runtime").cast(IntegerType()))

# Convert Released_Year to integer
df = df.withColumn("Released_Year", col("Released_Year").cast(IntegerType()))

# Fill other missing values
df = df.na.fill({
    "Meta_score": 0,
    "Certificate": "Unrated"
})

# Write cleaned data back to S3
df.write.mode("overwrite").parquet("s3://akhil-pipeline/imdb_cleaned/")
