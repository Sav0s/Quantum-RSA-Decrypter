import timeit

import run

if __name__ == '__main__':
    print(f"\n\n\n Performance Measuring ended. It took: {timeit.timeit(run.main, number=5)}s")
