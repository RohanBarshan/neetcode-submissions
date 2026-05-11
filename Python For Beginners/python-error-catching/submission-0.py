def divide_numbers(a: str, b: str) -> None:
    try:
        number1 = int(a)
        number2 = int(b)
        result =  number1 / number2
        print(result)
    except Exception as error:
        print("An error occurred:", error)


divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
