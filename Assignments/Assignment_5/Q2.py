def rectangle_stats(length, width):

    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter 

length = int(input("What is the length?: "))
width = int(input("What is the width?: "))

area, perimeter = rectangle_stats(length, width)

print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
