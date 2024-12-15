from random import randint as ri
print('Программа загадала число от 1 до 10, угадайте его с трех попыток!')
x, k = ri(1, 10), 1
while int(input()) != x:
    if k == 3:
        print('Попытки кончились!')
        exit()
    k += 1;
    print('Попробуйте еще раз!')
print('Вы угадали!')