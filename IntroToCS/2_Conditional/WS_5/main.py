# Diseñe un programa que lea tres longitudes y determine
#  si forman o no un triángulo. Si es un triángulo, determine
#  de qué tipo de triángulo se trata. Considere que para formar
#  un triángulo se requiere que el lado mayor sea menor que la
#  suma de los otros dos lados.

def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Try again.")


def triangle():
    l1 = get_data()
    l2 = get_data()
    l3 = get_data()
    if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
        print("The numbers do not form a triangle.")
    elif l1 == l2 and l2 == l3:
        print("The numbers form an equilateral triangle.")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("The numbers form an isosceles triangle.")
    else:
        print("The numbers form a scalene triangle.")


def main():
    triangle()


if __name__ == "__main__":
    main()
