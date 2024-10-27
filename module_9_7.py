def is_prime(func):
    def wrapper(*args, **kwargs):
         result = func(*args, **kwargs)
         is_p = True
         for i in range(2, result):
             if result % i == 0:
                 is_p = False
         if is_p is False:
             print('Составное')
         else:
             print('Простое')
         return result
    return wrapper


@is_prime
def sum_three(*args):
    sm = sum(args)
    return sm


result = sum_three(2, 3, 6)
print(result)
