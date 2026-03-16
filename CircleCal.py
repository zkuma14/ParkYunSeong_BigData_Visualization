import math

radius = float(input("원의 반지름을 입력하세요: "))

circumference = 2 * math.pi * radius

area = math.pi * (radius ** 2)

print(f"반지름이 {radius}인 원의:")
print(f"- 둘레: {round(circumference, 2)}")
print(f"- 넓이: {round(area, 2)}")