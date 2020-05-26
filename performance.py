import timeit

import run

if __name__ == '__main__':
    print(f"\n\n\n Performance Measuring ended. It took: {timeit.repeat(setup=run.main, repeat=5)}s")
