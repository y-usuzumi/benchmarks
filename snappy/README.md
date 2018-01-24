Snappy
---

[Introduction](https://github.com/google/snappy)

## Description

### TTR

The benchmark involves three sets of TTR, each containing 1, 32 and 32 TTRs.

| File | Original size | Size of .sz |
|------|---------------|-------------|
|    1 |          1084 |         822 |
|    2 |         27003 |        4948 |
|    3 |         26587 |        4948 |


## Compression

### Round 1

Compress the three TTR text files. Repeat for 100000 times.

### Round 2

Compress a concatenation of 1000 repetitive content of each TTR text files. Repeat for 100 times.


## Decompression

Decompress the three TTR .sz files. Repeat for 100000 times.
