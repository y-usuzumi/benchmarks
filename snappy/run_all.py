import os
import traceback
import subprocess
import json

_CURR_DIR = os.path.dirname(__file__)
_COMPRESSION_RUNTIMES = ['cpython27', 'pypy2', 'go', 'rust']
_COMPRESSION_TESTS = {
    'round_1': {
        'concat_repetitions': 1,
        'iterations': 10000,
        'files': ['1.ttr.text', '2.ttr.text', '3.ttr.text']
    },
    'round_2': {
        'concat_repetitions': 1000,
        'iterations': 10,
        'files': ['1.ttr.text', '2.ttr.text', '3.ttr.text']
    }
}
_DECOMPRESSION_RUNTIMES = ['cpython27', 'pypy2', 'go', 'rust']
_DECOMPRESSION_TESTS = {
    'round_1': {
        'iterations': 10000,
        'files': ['1.ttr.kpack.sz', '2.ttr.kpack.sz', '3.ttr.kpack.sz']
    }
}

def run_compression(test_file, runtime, concat_repetitions, iterations):
    test_dir = os.path.join(_CURR_DIR, 'compress')
    cwd = os.path.join(test_dir, runtime)
    cmd = 'run.sh'
    test_file = os.path.join(_CURR_DIR, '../_input_data', test_file)
    try:
        p = subprocess.Popen(
            ['sh', cmd, test_file, str(concat_repetitions), str(iterations)],
            stdout=subprocess.PIPE,
            cwd=cwd
        )
        output, _ = p.communicate()
        start_time, end_time = [float(o) for o in output.split()]
    except subprocess.CalledProcessError:
        traceback.print_exc()
        start_time, end_time = 0, 0
    return start_time, end_time


def run_decompression(test_file, runtime, iterations):
    test_dir = os.path.join(_CURR_DIR, 'decompress')
    cwd = os.path.join(test_dir, runtime)
    cmd = 'run.sh'
    test_file = os.path.join(_CURR_DIR, '../_input_data', test_file)
    p = subprocess.Popen(
        ['sh', cmd, test_file, str(iterations)],
        stdout=subprocess.PIPE,
        cwd=cwd
    )
    output, _ = p.communicate()
    start_time, end_time = [float(o) for o in output.split()]
    return start_time, end_time


def main():
    # Compression
    compression_result, decompression_result = {}, {}
    for runtime in _COMPRESSION_RUNTIMES:
        runtime_result = compression_result.setdefault(runtime, {})
        for round_id, round_cfg in _COMPRESSION_TESTS.items():
            round_result = runtime_result.setdefault(round_id, {})
            cr, it, files = [round_cfg[k] for k in ['concat_repetitions', 'iterations', 'files']]
            for f in files:
                print("%s / %s / %s" % (runtime, round_id, f))
                file_result = round_result.setdefault(f, {})
                start_time, end_time = run_compression(f, runtime, cr, it)
                file_result['elapsed'] = end_time - start_time

            # Round 2: 1000 x 10
    for runtime in _DECOMPRESSION_RUNTIMES:
        runtime_result = decompression_result.setdefault(runtime, {})
        for round_id, round_cfg in _DECOMPRESSION_TESTS.items():
            round_result = runtime_result.setdefault(round_id, {})
            it, files = [round_cfg[k] for k in ['iterations', 'files']]
            for f in files:
                print("%s / %s / %s" % (runtime, round_id, f))
                file_result = round_result.setdefault(f, {})
                start_time, end_time = run_decompression(f, runtime, it)
                file_result['elapsed'] = end_time - start_time

    print(json.dumps(compression_result, indent=4))
    print(json.dumps(decompression_result, indent=4))


if __name__ == '__main__':
    main()