from pyspark.sql.types import *
from pyspark.sql.functions import *
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

print "PARQUET partitions org_id"
start = timeit.timeit()
df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
df.write.partitionBy('org_id').parquet('/Users/code/Documents/spark/data/write/partitions/org_id/parquet/', mode='overwrite')
end = timeit.timeit()
print "PARQUET partitions org_id time:" + str(end - start)

# print "PARQUET 100 partitions"
# start = timeit.timeit()
# df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
# df.write.parquet('/Users/code/Documents/spark/data/write/partitions/100/parquet/', mode='overwrite', numPartitions=100)
# end = timeit.timeit()
# print "PARQUET time:" + str(end - start)

# print "PARQUET 50 partitions"
# start = timeit.timeit()
# df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
# df.write.parquet('/Users/code/Documents/spark/data/write/partitions/50/parquet/', mode='overwrite', numPartitions=50)
# end = timeit.timeit()
# print "PARQUET time:" + str(end - start)

# print "PARQUET 25 partitions"
# start = timeit.timeit()
# df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
# df.write.parquet('/Users/code/Documents/spark/data/write/partitions/25/parquet/', mode='overwrite', numPartitions=25)
# end = timeit.timeit()
# print "PARQUET time:" + str(end - start)