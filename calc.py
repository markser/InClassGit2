

def calc(a,b):
    calcSum = a + b
    # print("Addition: {0}".format(calcSum))
    calcSub = a - b
    # print("Subtraction: {0}".format(calcSub))
    calcMul = a * b
    # print("Multiplication: {0}".format(calcMul))
    calcDiv = a / b
    # print("Division: {0}".format(calcDiv))

    # print([calcSum,calcSub,calcMul,calcDiv])

    return [calcSum,calcSub,calcMul,calcDiv]
    # sumOfList = sum(calcList)

    # print(sumOfList)

# calc(3,3)


def main():
    x = int(input("Enter a first value: "))
    y = int(input("Enter a second value: "))

    calc(x,y)


if __name__ == "__main__":
    main()
