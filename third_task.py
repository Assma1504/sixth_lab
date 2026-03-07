def check_magic_date():
    
    try:
        year = int(input("Please enter the year: "))
        month = int(input("Please enter the month: "))
        day = int(input("Please enter the day: "))
        lastTwoDigits = year % 100
        productMontDay = month * day
        if productMontDay == lastTwoDigits :
            print("It's a magic year")
        else: 
            print("Ops,  it's not magic")
    except ValueError:
        print("Please enter a valid number")

check_magic_date()