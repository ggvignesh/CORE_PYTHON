#11. Implement a class-based decorator (using __init__ and __call__) called RetryOnException that retries the decorated function up to n times if it raises a specific exception type. The exception type and number of retries should be passed to the decorator factory.
# Demonstrate it on a function that randomly fails.
import random
import functools
class RetryOnException:
    def __init__(self, exception_type, retries):
        self.exception_type = exception_type
        self.retries = retries

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(self.retries + 1):
                try:
                    return func(*args, **kwargs)
                except self.exception_type as e:
                    if attempt == self.retries:
                        print("All retries failed.")
                        raise
                    print(
                        "Attempt",
                        attempt + 1,
                        "failed. Retrying..."
                    )
        return wrapper

@RetryOnException(ValueError, 3)
def random_task():
    number = random.randint(1, 3)
    if number == 1:
        raise ValueError("Random failure occurred.")
    print("Task completed successfully.")
try:
    random_task()
except ValueError:
    print("Final result: Function failed after all retries.")