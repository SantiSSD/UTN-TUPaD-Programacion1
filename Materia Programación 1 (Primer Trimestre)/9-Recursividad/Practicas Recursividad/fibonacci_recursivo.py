def fibonacci_recursivo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    else:
        return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num -2)


print(fibonacci_recursivo(10))