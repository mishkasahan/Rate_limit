from datetime import datetime,timedelta
import time


def rate_limit(max_calls, period):
    last_reset_time = datetime.now()
    call_count = 0

    def reset_counter():
        nonlocal call_count
        nonlocal last_reset_time
        if call_count == max_calls:
            if last_reset_time + timedelta(seconds=period) < datetime.now():
                last_reset_time = datetime.now()
                call_count = 0
            else:
                print("Ви перевищили кількість викликів фунції для заданого періоду")


    def decorator(func):
        def wrapper(*args,**kwargs):
            nonlocal call_count
            reset_counter()
            if max_calls > call_count:
                func(*args, **kwargs)
                call_count += 1
                print(call_count)
        return wrapper
    return decorator


@rate_limit(3,4)
def pryvit(name: str):
    print(f"Hello {name}")


pryvit("Misha")
time.sleep(3)
pryvit("Petro")
pryvit("Marko")
pryvit("Ksenja")
time.sleep(3)
pryvit("Lana")
