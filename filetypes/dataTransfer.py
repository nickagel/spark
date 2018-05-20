from pyspark.sql.types import *
import timeit
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark Basic Write different file types") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

schema = StructType(fields=[
    StructField(name='username',         dataType=StringType(),     nullable=False),
    StructField(name='creation_date',    dataType=StringType(),     nullable=False),
    StructField(name='org_id',           dataType=IntegerType(),    nullable=False),
    StructField(name='phone',            dataType=StringType(),     nullable=False)
])

print "CSV"
start = timeit.timeit()
df = spark.read.csv('/Users/code/Documents/spark/data/read/sample.csv', schema, '|')
df.write.csv('/Users/code/Documents/spark/data/write/dataTransfer/csv/', mode='overwrite')
end = timeit.timeit()
print "CSV time:" + str(end - start)

print "PARQUET"
start = timeit.timeit()
df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
df.write.parquet('/Users/code/Documents/spark/data/write/dataTransfer/parquet/', mode='overwrite')
end = timeit.timeit()
print "PARQUET time:" + str(end - start)


print "JSON"
start = timeit.timeit()
df = spark.read.json('/Users/code/Documents/spark/data/read/sample.json')
df.write.json('/Users/code/Documents/spark/data/write/dataTransfer/json/', mode='overwrite')
end = timeit.timeit()
print "JSON time:" + str(end - start)
