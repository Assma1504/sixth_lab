def devision_By_hundred():
    
    try:
        userNumber = int(input("Enter a number: "))
        result = 100 / userNumber
        print(result)
    except ZeroDivisionError:
        print("can't devide by 0")
    except ValueError:
        print("Please enter a number")

devision_By_hundred()
    