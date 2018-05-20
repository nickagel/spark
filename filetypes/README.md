# File types

Currently only read / write

- text file
- squence file
- parquet file
- avro file
- json file
- hbase

## CSV file

## sequence file

## parquet file

provides efficient data compression and encoding schemas w/ enhanced performance to handle comple data in bulk.

Built on record-shredding and assembly algorithm. This algorithm ues a column striping algorithm to only split the data into columns allowing only relevant data to be read in a query. When building a record the Record assembly algorithm only queries relevant row and ignores the rest of data without requiring the read. 

column oriented data serialization standard for efficient data analytics

optimized for Run-length-encoding, dictionary, and bit packing when compression is applied.

Pro: implements a hybrid of bit packing and RLE based on what produces best compression results

partitioning can be applied as well


* run-length-encoding: duplicate rows are stored once along w/ # of occurrences. 

* bit packing: stores integers into same space to make storage more efficient

* dictionary encoding: dyanamically encodes data w/ small unique values to increase compression and speed


### why we use parquet
- queries fetch specific column values without reading entire row of data 
- compression techniques can be applied to "like" date in the same column
- multiple encoding techniques are applied based on what is more performant
- good flexibility, fast data ingenstion, fast random lookup and scalable

## avro file

data serialization standard for compact binary format widely used for storing persistent data. 

Pros: 
Fast at serialisations & deserialization for ingestion performance. Directory based partitioning can be applied to easily navigate collections of interest

Cons: no internal index, last updated in 2017 - clearly not maintained

## json file

## Databases in general

### habase
scalable and distributed nosql database that stores key value pairs. provides quick access to records

### JDBC 
postgresql


## apache kudu





# Data ingestion
real time importing of data for immediate use

Avro has lightweight encoder will achieve best performance on data ingenstion

Parquet is second to avro

# space utilization
storing the same amount of data across file systems

ON average parquet takes up the least amount of space uncompressed. 

# Random data lookup latency

parquet, kudu, database have minimal datalookup because of the built in indexing

Parquet achieves low latency because of its column formating where scanning sets of data rather than reading through full sets -> w/ partitioning this file type can exceed expectations

# scan rate
When pefroming queries on datasets parquet excels here because it reads pertenant data in each column. 

# findings from tests
Parquet performas better
- not ingestion, query, write