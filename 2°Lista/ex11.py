def frag1(n):
    for i in range(n):
        print(i)

def frag2(n):
    for i in range(0, n, 2):
        print(i)

def frag3(n):
    for i in range(0, n, 2):
        print(i)
        i -= 1 
n = int(input("Digite o valor de n: "))
print("Fragmento 1:")
frag1(n)
print("\nFragmento 2:")
frag2(n)
print("\nFragmento 3:")
frag3(n)
