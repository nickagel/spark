# compression
The gola w/ compression is to save storage space and network overhead
Types of compression
- gzip
- lzo
- bizp2
- zlib
- snappy

## gzip
compression speed
- fast
effectiveness on text
- high

## lzo
compression speed
- very fast
effectiveness on text
- Medium
Note: needs to be installed on every node

## bizp2
compression speed
- slow
effectiveness on text
- very high

## zlib
compression speed
- slow
effectiveness on text
- medium

## snappy
compression speed
- very fast
effectiveness on text
- low

### Why
- We currently use snappy for our parquet files. This makes sense because it compresses the files incredibly fast. We don't need it for text
- CSV we use gzip -> text file compression is fast and more efficient for text files
