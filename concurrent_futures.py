from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
from time import perf_counter, sleep
from functools import wraps


def chronomeasure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        perf_time = perf_counter() - start_time
        ex_type = ""
        if len(args) >= 3:
            if issubclass(args[-1], Executor):
                ex_type = f" with {args[-1].__name__}"
        print(f"{func.__name__}{ex_type} ran for {perf_time:.8f}")
        return result

    return wrapper


@chronomeasure
def power_multi(arg_list, power, ex_type):
    result_list = []
    with ex_type(max_workers=4) as executor:
        for input_item in arg_list:
            future = executor.submit(pow, input_item, power)
            result_list.append(future.result())
    return result_list


@chronomeasure
def power_single(arg_list, power):
    print(f"running single ...")
    return [input_item ** power for input_item in arg_list]


if __name__ == "__main__":
    
    list_of_stuff = [13829, 4839, 9048, 3433442, 35583, 8928248, 834757]
    print(power_multi(list_of_stuff, 9, ThreadPoolExecutor))
    sleep(1)
    print(power_multi(list_of_stuff, 9, ProcessPoolExecutor))
    sleep(1)
    print(power_single(list_of_stuff, 9))


    l = [1, 2, 3]
    print(reversed(l))
