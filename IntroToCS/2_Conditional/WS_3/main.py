# Dada una circunferencia, teniendo en cuenta su centro (x1,y1) y su radio r,
# y un punto (x2,y2) en el plano cartesiano,
# determine si este punto (x2,y2) está sobre la circunferencia o adentro de ella.


def get_data(string):
    while True:
        try:
            data = float(
                input(f"\033[0;33mIngrese el valor de {string}: \033[0m"))
            return data
        except ValueError:
            print("\033[0;31mEl dato ingresado no es un número.\033[0m")


def point_in_circumference():
    x1 = get_data("x1")
    y1 = get_data("y1")
    r = get_data("r")
    x2 = get_data("x2")
    y2 = get_data("y2")
    res_op = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if res_op == r**2:
        return True
    else:
        return False


def main():
    if point_in_circumference():
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()
