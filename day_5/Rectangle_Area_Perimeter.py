def Rectangle(width, length):
 
    # calculating area of The Rectangle
    Area = width * length
 
    # calculating Perimeter of The Rectangle
    Perimeter = 2 * (width + length)
 
    print "Area of a Rectangle is:    %.2f" %Area
    print "Perimeter of Rectangle is: %.2f" %Perimeter

a = int(raw_input("Enter Width of The Rectangle :"))
b = int(raw_input("Enter length of The Rectangle:"))
Rectangle(a, b)





