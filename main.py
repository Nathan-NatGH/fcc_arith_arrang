
# given_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
given_list = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]


def arithmetic_arranger(raw_raw_list, compute):
    raw_list = [item.split() for item in raw_raw_list]
    undesirables_list = ['*', '/']

    # clean the data (apply constraints)
    for string in raw_list:
        for _ in undesirables_list:
            if _ in string:
                print("Error: Operator must be '+' or '-'")
                quit()
        if not string[0].isdigit() or not string[2].isdigit():
            print("Error: Numbers must only contain digits")
            quit()
        if len(string[0]) > 4 or len(string[2]) > 4:
            print("Error: Numbers cannot be more than four digits")
            quit()
        if len(raw_raw_list) > 5:
            print("Error: Too many problems")
            quit()

    top = [item[0] for item in raw_list]
    operator = [item[1] for item in raw_list]
    bottom = [item[2] for item in raw_list]
    mathtop = top[:]
    mathbottom = bottom[:]

    for i in range(len(raw_raw_list)):
        if len(bottom[i]) > len(top[i]):
            bottom[i] = operator[i] + ' ' + bottom[i]
        elif len(bottom[i]) < len(top[i]):
            bottom[i] = operator[i] + ' ' * (len(top[i]) - len(bottom[i]) + 1) + bottom[i]
        else:
            bottom[i] = operator[i] + ' ' + bottom[i]

    # printouts (no math)
    for i in range(len(bottom)):
        width = len(bottom[i])
        print(top[i].rjust(width), end=4*' ')

    print()

    for i in range(len(bottom)):
        width = len(bottom[i])
        print(bottom[i].rjust(width), end=4*' ')

    print()

    dashes = [len(x)*'-' for x in bottom]

    for i in range(len(bottom)):
        print(dashes[i], end=4*' ')

    # printouts (with math -- optional)
    print()

    while compute is True:
        for i in range(len(bottom)):
            width = len(bottom[i])
            if operator[i] == '+':
                sum = int(mathtop[i]) + int(mathbottom[i])
                print(str(sum).rjust(width), end=4*' ')
            else:
                diff = int(mathtop[i]) - int(mathbottom[i])
                print(str(diff).rjust(width), end=4 * ' ')
        compute = False

    print()


arithmetic_arranger(given_list, True)