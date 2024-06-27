import math

# Öklid mesafesi için bir fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

points = []
n = int(input("Kaç tane nokta gireceksiniz? "))

for i in range(n):
    x = float(input(f"{i+1}. noktanın x koordinatını girin: "))
    y = float(input(f"{i+1}. noktanın y koordinatını girin: "))
    points.append((x, y))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print(f"Minimum Öklid mesafesi: {min_distance}")
