import math

left_side=float(input("Enter the first leg of the right triangle:"))
right_side=float(input("Enter the second leg of the right triangle:"))

third_side=math.sqrt(left_side**2 + right_side**2)

third_side=round(third_side,3)

area= (left_side * right_side)/2
area=round(area,3)
print(third_side)
print(area)
