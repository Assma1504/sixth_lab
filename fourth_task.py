def check_happy_number():
    number = input("Please enter a number which composed from even didgits: ")
    while len(number) % 2 != 0:
        number = input("Please enter a number which composed from even didgits: ")
    else:
        halfLentgh =int(len(number)/ 2)
        summFirstHalf = 0
        summSecondHalf = 0
        firstCounter = 0
        secondCounter = halfLentgh
        while firstCounter <= halfLentgh - 1:
            summFirstHalf += int(number[firstCounter])
            firstCounter += 1
        while secondCounter <= len(number) - 1:
            summSecondHalf += int(number[secondCounter])
            secondCounter += 1
        
        if summFirstHalf == summSecondHalf:
            print(f"Билет с номером {number} — счастливый")
        else: 
            print(f"Билет с номером {number} не является счастливым")

check_happy_number()