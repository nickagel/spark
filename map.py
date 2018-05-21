
# map allows simple lambda functions to be conducted on each individual value 
# paralleilize allows the list/array to be operated in parrallel. Each core can only conduct one job at a time.

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