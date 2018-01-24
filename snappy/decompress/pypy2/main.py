import sys
import time
import snappy


def decompress(data, iterations=1):
    i = 0
    while i < iterations:
        decompressor = snappy.StreamDecompressor()
        _ = decompressor.decompress(data)
        i += 1


def main():
    f, iterations = sys.argv[1], int(sys.argv[2])
    with open(f, 'rb') as f:
        data = f.read()
    start = time.time()
    print("%.6f" % start)
    decompress(data, iterations=iterations)
    end = time.time()
    print("%.6f" % end)

if __name__ == '__main__':
    main()
