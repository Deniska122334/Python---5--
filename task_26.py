def rec_step(a,b):
    if b < 20:
        if b > 0 and isinstance(b, int):
            print(a**b)
            rec_step(a,b+1)
rec_step(2,2)













# def rec(a, b):
#     0 == 0
#     return 1
# return rec(a, b - 1)

# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# print(rec(a, b))