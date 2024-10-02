import asyncio
import inspect
import threading


def run_in_thread(func):
    def wrapper(*args, **kwargs):
        if inspect.iscoroutinefunction(func):
            _thread = threading.Thread(target=asyncio.run, args=(func(*args, **kwargs),))
        else:
            _thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        _thread.start()

    return wrapper


if __name__ == "__main__":
    import time

    @run_in_thread
    def test(test=1):
        time.sleep(test)
        print("Hello, world!")

    test(test=1)
    print("Main thread")
    time.sleep(2)
