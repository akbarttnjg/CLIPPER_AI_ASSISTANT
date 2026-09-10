"""Production benchmark foundation."""
import time


def benchmark(task):
    start = time.perf_counter()
    result = task()
    return {
        "elapsed": time.perf_counter() - start,
        "result": result,
    }
