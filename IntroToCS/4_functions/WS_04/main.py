def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data


def padovan(n):
    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1

    for i in range(3, n+1):
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext

    return pNext


def main():
    n = get_data()
    print(padovan(n))


if __name__ == '__main__':
    main()
