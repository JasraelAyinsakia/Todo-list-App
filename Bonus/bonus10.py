try:
    width = float(input("Enter Rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width == length:
        exit("This looks like a square")
    area = width * length

    print(area)
except ValueError:
    print("please enter a number.")