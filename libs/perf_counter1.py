from time import perf_counter


start = perf_counter()
numbers = list(range(10**7))
end = perf_counter()

print(f'время выполнения (elapsed time): {(end - start)*10**3:.3f} мс')

