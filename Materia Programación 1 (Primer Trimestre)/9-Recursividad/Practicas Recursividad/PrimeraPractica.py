# def factorial_recur(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial_recur(x-1)
    

# print(factorial_recur(4))

def despegue(n):
    if n == 0:
        return print("Despegue")
    else:
        print(n)
        despegue(n - 1)


despegue(3)