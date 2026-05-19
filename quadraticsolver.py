while True:
    choice = input("Prnt? Yes/No [type 1/2]\n>")
    if choice == "1":
        print("x = [-b ± sqrt(b^2 - 4ac)] / 2a")
        break
    elif choice == "2":
        break
    else:
        print("Invalid input. Please enter Yes or No.")

while True:
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("This is not a quadratic equation.")
        else:
            discriminant = b ** 2 - 4 * a * c

            if discriminant > 0:
                root1 = (-b + discriminant ** 0.5) / (2 * a)
                root2 = (-b - discriminant ** 0.5) / (2 * a)
                print("Roots: ", root1," , ",root2)
            elif discriminant == 0:
                root = -b / (2 * a)
                print("Repeated root: ", root)
            else:
                print("Complex roots")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

    if input("Press 1 to quit\n>") == "1":
        break
