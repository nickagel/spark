
from pyspark import SparkContext
sc = SparkContext("local", "Simple App")
nums = sc.parallelize([1,2,3,4])
squared = nums.map(lambda x: x * x).collect()
for num in squared:
    print "%i " % (num)


nums = sc.parallelize([1,2,3,4])
squared = nums.map(lambda x: x / x + x).collect()
for num in squared:
    print "%i " % (num)