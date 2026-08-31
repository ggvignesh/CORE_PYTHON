#10. Write a decorator factory called rate_limit(max_calls, period_seconds) that allows a function to be called at most max_calls times within any period_seconds window. If the limit is exceeded, raise a RuntimeError with a clear message.
# Use time.time() to track the window.
import functools
import time
from collections import deque

def rate_limit(max_calls, period_seconds):
    call_times = deque()
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            while call_times and current_time - call_times[0] >= period_seconds:
                call_times.popleft()
            if len(call_times) >= max_calls:
                raise RuntimeError(
                    "Rate limit exceeded. Try again later."
                )
            call_times.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period_seconds=5)
def greet():
    print("Hello!")
try:
    greet()
    greet()
    greet()
    greet()
except RuntimeError as e:
    print("Error:", e)