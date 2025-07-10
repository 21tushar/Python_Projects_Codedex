print("==================")
print("Area Calculator 📐")
print("==================\n")

print("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Quit\n")

while True:
    shape = int(input("Which Shape: "))

    if shape in [1, 2, 3, 4, 5]:
        if shape == 1:
            side = float(input("\nEnter Side: "))
            print(f"\nArea of Square is: {side ** 2}")
        elif shape == 2:
            length = float(input("\nEnter Length: "))
            width = float(input("Enter width: "))
            print(f"\nArea of Rectangle is: {length * width}")
        elif shape == 3:
            height = float(input("\nEnter height: "))
            base = float(input("Enter base: "))
            print(f"\nArea of Triangle is: {(height * base) / 2}")
        elif shape == 4:
            pi = 3.14
            radius = float(input("\nEnter radius: "))
            print(f"\nArea of Circle is: {pi * radius ** 2}")
        elif shape == 5:
            print("\nQuitting...")
        break
