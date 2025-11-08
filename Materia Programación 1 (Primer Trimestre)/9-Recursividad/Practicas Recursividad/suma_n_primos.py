def num_primos(num):
    if num <= 1:
        return False
    for i in range(2, int(num **0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_num_primos(num):
    if num == 1:
        return 0
    elif num_primos(num):
        return num + sum_num_primos(num -1)
    else:
        return sum_num_primos(num -1)