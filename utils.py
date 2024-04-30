from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

def load_data(file_path):
    spark = SparkSession.builder.appName("Get Data").getOrCreate()
    data = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(file_path)
    return data

def save_data(data, file_path):
    data.toPandas().to_csv(file_path, index=False)