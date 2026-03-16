#=============== First Option ============================
# def check_devision(num):
#     if num % 3 == 0:
#         print(f"{num} can be devided by 3")
#     else:
#         print(f"{num} can't be devided by 3")

# check_devision(15)

#=============== Second Option ============================
def check_division_by_three():
    userNumber =int(input("Please a number: "))
    if userNumber % 3 == 0:
        print(f"{userNumber} can be devided by 3")
    else:
        print(f"{userNumber} can't be devided by 3")

check_division_by_three()   