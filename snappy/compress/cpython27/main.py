import sys
import time
from itertools import repeat
import snappy


def compress(data, iterations=1):
    i = 0
    while i < iterations:
        compressor = snappy.StreamCompressor()
        _ = compressor.add_chunk(data)
        i += 1


def main():
    f, concat_repetitions, iterations = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    with open(f, 'rb') as f:
        data = f.read()
    data = ''.join(repeat(data, concat_repetitions))
    start = time.time()
    print("%.6f" % start)
    compress(data, iterations=iterations)
    end = time.time()
    print("%.6f" % end)

if __name__ == '__main__':
    main()
