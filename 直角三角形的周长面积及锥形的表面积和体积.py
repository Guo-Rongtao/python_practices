import math

def calculate_perimeter(base, height):
    return base + height + math.sqrt(base**2 + height**2)

def calculate_area(base, height):
    return 0.5 * base * height

def calculate_surface(base, height):
    slant = math.sqrt(base**2 + height**2)
    return math.pi * base * (base + slant)

def calculate_volume(base, height):
    return (math.pi * base**2 * height) / 3

def main():
    base = eval(input("Width of the right triangle'base: "))
    height = eval(input("Height of the right triangle'base: "))

    area = calculate_area(base, height)
    perimeter = calculate_perimeter(base, height)
    surface = calculate_surface(base, height)
    volume = calculate_volume(base, height)

    print('*^*'*20)
    print("%-40s = %9.2f" % ("Area of the right triangle", area))
    print("%-40s = %9.2f" % ("Perimeter of the right triangle", perimeter))
    print("%-40s = %9.2f" % ("Surface of the cone", surface))
    print("%-40s = %9.2f" % ("Volume of cone", volume))

if __name__ == "__main__":
    main()
