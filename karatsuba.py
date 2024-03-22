def multiplication(x, y):
    a = str(x)                            
    b = str(y)                            
    length = max(len(a), len(b))           # Визначення кількості цифр у числах

    if length == 1:                        # Умова зупинки рекурсії
        return int(x) * int(y)
    
    new_length = length // 2
    a1 = a[:-new_length]
    a0 = a[-new_length:]                   # a = a1 * (10 ** 0.5n) + a0
    b1 = b[:-new_length]                   # b = b1 * (10 ** 0.5n) + b0
    b0 = b[-new_length:]
    if len(a1) == 0:                       # Якщо нічого не залишилось, то замінюємо на 0
        a1 = 0
    if len(a0) == 0:
        a0 = 0
    if len(b1) == 0:
        b1 = 0
    if len(b0) == 0:
        b0 = 0

    m1 = multiplication(a1, b1)           # Рекурсивні множення
    m2 = multiplication(a1, b0)
    m3 = multiplication(a0, b1)
    m4 = multiplication(a0, b0)

    return (m1*(100**new_length) + m2*(10**new_length) + m3*(10**new_length) + m4)
    

def karatsuba (x, y):
    a = str(x)                            
    b = str(y)                            
    length = max(len(a), len(b))           # Визначення кількості цифр у числах

    if length == 1:                        # Умова зупинки рекурсії
        return int(x) * int(y)
    
    new_length = length // 2
    a1 = a[:-new_length]
    a0 = a[-new_length:]                   # a = a1 * (10 ** 0.5n) + a0
    b1 = b[:-new_length]                   # b = b1 * (10 ** 0.5n) + b0
    b0 = b[-new_length:]
    if len(a1) == 0:                       # Якщо нічого не залишилось, то замінюємо на 0
        a1 = 0
    if len(a0) == 0:
        a0 = 0
    if len(b1) == 0:
        b1 = 0
    if len(b0) == 0:
        b0 = 0

    s1 = int(a1) + int(a0)
    s2 = int(b1) + int(b0)
    m1 = karatsuba(a1, b1)                # Рекурсивні множення
    m2 = karatsuba(a0, b0)
    m3 = karatsuba(s1, s2)
    s3 = m1 + m2

    return (m1*(100**new_length) + (m3 - s3)*10**new_length + m2)
    
while True:
    n1 = int(input("Перше число: "))
    n2 = int(input("Друге число: "))
    print(f'Результат:      {multiplication(n1, n2)}')
    print(f'Метод Карацуби: {karatsuba(n1, n2)}')
    print('-'*50)