# imdb-aws-data-pipeline
IMDb Top 1000 Movie Data Pipeline using AWS S3, Glue, Athena &amp; QuickSight
Building a Data Pipeline with AWS: IMDb Top 1000 Movies Project

In this blog, we'll walk through how to build a complete data pipeline using AWS services. We'll use IMDb's Top 1000 movies dataset and clean, transform, query, and visualize it using Amazon S3, AWS Glue, Amazon Athena, and Amazon QuickSight.
Step 1: Store Data in Amazon S3
We start by uploading our raw dataset imdb_top_1000.csv to an S3 bucket named akhil-pipeline (you can name your bucket differently, akhil is used here as an example).
Download data from- 
 To Do It:
Go to the S3 service in the AWS Console.

2. Click Create bucket (if you don't have one already).
3. Name your bucket (e.g., akhil-pipeline) and choose your region.
4. Click Create bucket.
5. Open the bucket and click Upload.
6. Upload the imdb_top_1000.csv file either to the root or inside a folder like raw/.
Make sure:
The file is placed in the folder or root directory like: s3://akhil-pipeline/imdb_top_1000.csv
It's accessible via IAM roles used by Glue and Athena.

 Step 2: Create Glue Database
Navigate to AWS Glue > Data Catalog > Databases

2. Click "Add database"
3. Name it: imdb_pipeline_db
4. Click Create
This creates a logical container to organize your tables.
 Step 3: Create a Glue Crawler
Go to AWS Glue > Crawlers
Click "Add crawler"

3. Name it: imdb-crawler
 2. Data store: Choose S3, and provide path: s3://akhil-pipeline/imdb_top_1000.csv
3. IAM Role: Choose existing or create a new IAM role with S3 read access
4. Database: Select imdb_pipeline_db
5. Run frequency: Select Run on demand
6. Click Finish and Run crawler
This will catalog the CSV file into a table in Glue Data Catalog.
️ Step 4: Create an AWS Glue Job for Data Cleaning
To transform and clean the raw IMDb data:
Go to AWS Glue > Jobs
Click "Add job"
Enter Job Name: clean-imdb-job
Choose or create an IAM role with access to Glue, S3, and logs
Click Next until you reach the Script options section
Choose Script editor

7. Select Spark as the language
8. run code 
9 .Save the script and give it a name.

10. Choose number of workers (start with 2–3 for simple jobs).
11. Click Save and Run Job
This job will transform and clean the data and store the structured output in Parquet format.
 Step 5: Query Data with Amazon Athena
Open Amazon Athena

2. Set a query result location (S3 folder) if prompted
3.Choose the Database: imdb_pipeline_db
4. Query the cleaned data:
SELECT * FROM imdb_cleaned_table LIMIT 10;
Make sure the cleaned Parquet table is added to Glue and re-crawled if needed.
5. Output of data will be showed below

 Step 6: Visualize in Amazon QuickSight
Go to Amazon QuickSight

Choose Datasets > New Dataset
Select Athena as the data source

Choose imdb_pipeline_db and select the cleaned table

Start building visuals (charts, dashboards, etc.)

 Conclusion
You've successfully built a complete AWS data pipeline:
Stored raw data in S3
Cataloged and cleaned it using Glue with pyspark
Queried with Athena
Visualized with QuickSight

This is a powerful, serverless, and scalable way to manage data analytics in the cloud
