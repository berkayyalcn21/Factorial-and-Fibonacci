while True:
    number = int(input("Enter number: "))
    if number == 0:
        print("Factorial of number 1")
    else:
        result = 1
        for i in range(number):
            print(i)
            result = result * (i+1)
            print("Factorial of number {}".format(result))