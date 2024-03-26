def dodawanie(x):

    a = x

    for i in range(5):

        a *= i

    return a

print(dodawanie(2))
print(dodawanie(3)+4*dodawanie(5))
