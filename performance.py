import timeit

import run
from numpy import mean

if __name__ == '__main__':
    executionCount = 10
    times = list()
    success = list()

    for _ in range(executionCount):
        starttime = timeit.default_timer()
        success.append(run.computate())
        times.append(timeit.default_timer() - starttime)
        
    mean = mean(times)
    successrate = success.count(True)
    print("The average time is: %.2f" % mean)
    print(f"{successrate} out of {executionCount} computated the factor correctly")
