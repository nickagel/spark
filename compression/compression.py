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

print "PARQUET compression snappy"
start = timeit.timeit()
df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
df.write.partitionBy('org_id').parquet('/Users/code/Documents/spark/data/write/compression/snappy/parquet/', mode='overwrite', compression="snappy")
end = timeit.timeit()
print "PARQUET compression snappy time:" + str(end - start)

print "PARQUET compression gzip"
start = timeit.timeit()
df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
df.write.partitionBy('org_id').parquet('/Users/code/Documents/spark/data/write/compression/gzip/parquet/', mode='overwrite', compression="gzip")
end = timeit.timeit()
print "PARQUET compression gzip time:" + str(end - start)

# print "PARQUET compression lzo"
# start = timeit.timeit()
# df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
# df.write.partitionBy('org_id').parquet('/Users/code/Documents/spark/data/write/compression/lzo/parquet/', mode='overwrite', compression="lzo")
# end = timeit.timeit()
# print "PARQUET compression lzo time:" + str(end - start)

# print "PARQUET compression zlib"
# start = timeit.timeit()
# df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
# df.write.partitionBy('org_id').parquet('/Users/code/Documents/spark/data/write/compression/zlib/parquet/', mode='overwrite', compression="zlib")
# end = timeit.timeit()
# print "PARQUET compression zlib time:" + str(end - start)

# print "PARQUET compression bizp2"
# start = timeit.timeit()
# df = spark.read.format('parquet').load('/Users/code/Documents/spark/data/read/parquet/',schema=schema, inferSchema=False)
# df.write.partitionBy('org_id').parquet('/Users/code/Documents/spark/data/write/compression/bizp2/parquet/', mode='overwrite', compression="bizp2")
# end = timeit.timeit()
# print "PARQUET compression bizp2 time:" + str(end - start)

