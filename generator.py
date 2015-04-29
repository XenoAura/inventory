with open('numbers.txt', 'w') as f:
    for num in range(1, 100):
        if num < 10:
            f.writelines('DZ00000%s\n' % num)
        elif 10 <= num < 100:
            f.writelines('DZ0000%s\n' % num)
