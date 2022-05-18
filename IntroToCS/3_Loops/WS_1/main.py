# programa que lea un número entero n y muestre en pantalla
# los números pares entre 1 y n.
def main():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)


if __name__ == '__main__':
    main()
