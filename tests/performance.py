from memory_profiler import profile, memory_usage
from src.primes import is_prime, print_primes
import random
import timeit


@profile
def metricFunction():
    is_prime(random.randrange(1, 10000))


if __name__ == "__main__":
    execution_time = timeit.timeit(metricFunction, number=1)
    print(f"Execution time: {execution_time}")
