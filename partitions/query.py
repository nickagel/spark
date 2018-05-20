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

print "PARQUET Unpartitioned"
start = timeit.timeit()
df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
df.createOrReplaceTempView("parquet_unpartitioned")
sqlDF = spark.sql("SELECT username FROM parquet_unpartitioned where org_id = 98024")
sqlDF.show()
end = timeit.timeit()
print "PARQUET Unpartitioned time:" + str(end - start)


print "PARQUET Partitioned"
start = timeit.timeit()
df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/write/partitions/org_id/parquet/')
df.createOrReplaceTempView("parquet_partitioned")
sqlDF = spark.sql("SELECT username FROM parquet_partitioned where org_id = 98024")
sqlDF.show()
end = timeit.timeit()
print "PARQUET Partitioned time:" + str(end - start)
print "done"