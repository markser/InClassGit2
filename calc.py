

class calc():

    def add(a, b):
        return a + b
    
    # Function to subtract two numbers 
    def sub(a, b):
        return a - b
    
    # Function to multiply two numbers
    def mul(a, b):
        return a * b
    
    # Function to divide two numbers
    def div(a, b):
        return a / b


def main():
    x = int(input("Enter a first value: "))
    y = int(input("Enter a second value: "))

    calc(x,y)


if __name__ == "__main__":
    main()
