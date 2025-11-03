a = int(input("Enter a lucky number between 1 and 10: "))
match a:
    case 1:
        print("You won a iPhone")
    case 3:
        print("You won a SONY FX3")
    case 6:
        print("You won $5000")
    case _:
        print("Better luck next time") 