def get_data():
    while True:
        try:
            value = str(input())
            return value
        except ValueError:
            print("Caracter(es) invalido(s)")


def divisibles(l, r, k):
    counter = 0
    for i in range(l, r+1):
        if i % k == 0:
            counter += 1
    return counter


def main():
    a = get_data()
    array = a.split(" ")
    nums = list(map(lambda x: int(x), array))
    print(divisibles(nums[0], nums[1], nums[2]))


if __name__ == "__main__":
    main()
