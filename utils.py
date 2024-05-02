from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

def load_data(file_path):
    spark = SparkSession.builder.appName("Get Data").getOrCreate()
    df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(file_path)
    return df

def save_data(df, file_path):
    df.toPandas().to_csv(file_path, index=False)