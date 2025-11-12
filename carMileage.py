carList = list(map(str, input().strip()))
name = []
mileage = []
for i in carList:
    carName, carMileage = i.split("@")
    name.append(carName)
    mileage.append(float(mileage))
lowestMileage = mileage.index(min(mileage))
print(name[lowestMileage])