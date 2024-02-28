import time as t

def time_count(func):

    def time_func():
        start_time = t.perf_counter()
        func()
        end_time = t.perf_counter()
        total_time = end_time - start_time
        return print(f"TIME = {total_time}")
    return time_func()

try:
    @time_count
    def count_till():
        for x in range(0,1000000):
            print(x)
    count_till()
except:
    exit()
