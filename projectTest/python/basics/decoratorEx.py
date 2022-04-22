class decoratorEx():
    def multiply_and_Sum(func):
        def wrapper(num1, num2):
            print("Sum is :" + str(num1 + num2))
            return func(num1, num2)

        return wrapper

    # define the function
    def multiply(num1, num2):
        print(num1 * num2)

    # Execute
    add_multiply = multiply_and_Sum(multiply)
    add_multiply(5, 10)
    print("_______________")
    multiply(5, 10)