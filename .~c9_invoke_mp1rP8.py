"""
Your module description
"""
'''print("Python has three numeric data types; int, float, complex")
myValue=1
print((str(myValue)) + " is of type " + str(type(myValue)))

myString="this is a string data type"
print(myString + " is of type " + str(type(myString)))

x="hello "
y="world!!!!"
z=x+y
print(z)

name=input("What is Your name?\n")
print("Welcome to Python Coding "+name+"!!!")

color=input("what is your favorite color?\n")
animal=input("what is your favorite animal\n")
print("{}, you like {} {}".format(name,color,animal))'''


'''myFruitList=["Apple", "Mango", "Orange"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
myFruitList[2]="Berries"
print(myFruitList)

MyFinalFruitTuple=("Mango", "Berries", "Grapes")
print(MyFinalFruitTuple)
print(type(MyFinalFruitTuple))
print(MyFinalFruitTuple[2])


myFruitDictionary={
    "Brian": "Orange",
    "Sharon": "Banana",
    "Simon": "Grapes"
}
print(myFruitDictionary)
print(myFruitDictionary["Brian"])'''



'''#Categorizing Values
myMixedList=[123, 349847748, 1.25, True, "This is how mix data types", "45"]
for item in myMixedList:
    print("{} is of the data type{}".format(item, type(item)))'''



#Composite Data Types
import csv
import copy

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0.0,
    "mileage": 0
}

for key, value in myVehicle:
    print("{} : {}".format(key, value))
    
myInventoryList=[]

with open('learnerprac.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')