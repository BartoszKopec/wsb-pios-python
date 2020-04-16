while True:
    print()
    try:
        a = float(input("Write number a: "))
        b = float(input("Write number b: "))
        operation = input("Write operation type [+, -, /, *]: ")
        if operation in ["+", "-", "/", "*"]:
            try:
                print(eval(str(a) + operation + str(b)))
            except ZeroDivisionError:
                print("Can not divide by zero")
        else:
            print("Invalid operation given")
    except ValueError:
        print("No numbers provided")