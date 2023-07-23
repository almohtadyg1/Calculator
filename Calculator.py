import os

def clear():
    os.system('cls')

while True:
    try:
        print(f"""\nWhat Do You Want To Do:
            1) X + Y
            2) X - Y
            3) X × Y
            4) X ÷ Y
            5) X ^ Y
            6) Y√X
            7) X ≃ Y
            8) |X|
            9) X (<,=,>) Y""")
        what = input("What is your choice (1/2/3/4/5/6/7/8/9)?\n")
        if what == "1":
            x = float(input("X = "))
            y = float(input("Y = "))
            answer = x+y
        elif what == "2":
            x = float(input("X = "))
            y = float(input("Y = "))
            answer = x-y
        elif what == "3":
            x = float(input("X = "))
            y = float(input("Y = "))
            answer = x*y
        elif what == "4":
            x = float(input("X = "))
            y = float(input("Y = "))
            answer = x/y
        elif what == "5":
            x = float(input("X = "))
            y = float(input("Y = "))
            answer = x**y
        elif what == "6":
            x = float(input("X = "))
            y = float(input("Y = "))
            answer = x**(1/y)
        elif what == "7":
            x = float(input("X = "))
            to = int(input("How many digits to the right of the point? "))
            answer = round(x, to)
        elif what == "8":
            x = float(input("X = "))
            answer = abs(x)
        elif what == "9":
            x = float(input("X = "))
            y = float(input("Y = "))
            if x < y:
                answer = "X < Y"
            elif x == y:
                answer = "X = Y"
            elif x > y:
                answer = "X > Y"
        print(f"The answer is {answer}")
    except:
        print("Invalid Input!")

    cl = input("Clear History (Y/N)? ")
    if cl.lower() == "y" or cl.lower() == "yes":
        clear()
    else:
        pass
