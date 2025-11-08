def sum_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + sum_recursiva(num - 1 )
    


print(sum_recursiva(10))    