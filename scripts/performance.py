import timeit

from scripts import bruteforce

if __name__ == '__main__':
    print(f"\n\n\n Performance Measuring ended. It took: {timeit.timeit(bruteforce.main, number=5)}s")
