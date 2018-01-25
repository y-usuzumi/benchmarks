import sys
import time
from itertools import repeat
import snappy


def decompress(data, iterations=1):
    i = 0
    while i < iterations:
        _ = snappy.decompress(data)
        i += 1


def main():
    f, concat_repetitions, iterations = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    with open(f, 'rb') as f:
        data = f.read()
    data = ''.join(repeat(data, concat_repetitions))
    start = time.time() * 1e9
    print("%d" % start)
    decompress(data, iterations=iterations)
    end = time.time() * 1e9
    print("%d" % end)

if __name__ == '__main__':
    main()
