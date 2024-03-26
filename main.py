def dodawanie():

    a = 2

    for i in range(5):

        a *= i

    return a

print(dodawanie())
print(dodawanie()+4*dodawanie())
