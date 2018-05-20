# Partitions
Determine the number of files created on write
More partitions allow work to be distributed among more workers
- less data per partition
Fewer partitions allow work to be done in larger chunks
- more data per partition

two types of partitioning
- static -> provide number of partitions
- dynamic -> provide the column to partition on

spark can only run 1 concurrent task for every partition of an rdd
- have 1 core per partition minimum 

partitions are executed lazily -> not until action is called

Partitioning causes shuffling

## why does this matter
One of sparks biggest issues is memory management
- we use a specific size partition to minimize chance of memory issue
- This is a flaw that does not auto scale. We will have to manually repartition to a larger number of partitions
- can reduce i/o
- goal is to utilize our resources we have available 
