class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_data(string):
    while True:
        try:
            num = float(
                input(f"\033[1;33mInserte el valor {string}: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def ccw(A, B, C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def main():
    a1 = get_data(" de Ax")
    a2 = get_data(" de Ay")
    b1 = get_data(" de Cx")
    b2 = get_data(" de Cy")
    c1 = get_data(" de Cx")
    c2 = get_data(" de Cy")
    d1 = get_data(" de Dx")
    d2 = get_data(" de Dy")

    a = Point(a1, a2)
    b = Point(b1, b2)
    c = Point(c1, c2)
    d = Point(d1, d2)

    print(str(intersect(a, b, c, d)).lower())


if __name__ == '__main__':
    main()
