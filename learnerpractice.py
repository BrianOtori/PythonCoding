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



'''#Composite Data Types
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

with open('learnerpractice.csv') as csvFile:
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
    
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")'''
        
        
        
        #CONDITIONAL STATEMENTS
        #If statements
'''name=input("what is your name?\n")
userReply = input("Dear "+ name+", Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("Dear "+ name+", We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("Dear "+ name+", We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("Dear "+ name+", How many copies would you like? (Enter a number) ")
    print("Dear "+ name+", Here are your {} copies.".format(copies))
else:
    print("Dear "+ name+", Thank you, please come again.")'''
    
    
    
    #While Loop
'''import random
print("WELCOME TO TGE GUESS NAMBA MANIA!!!\n" "The rules are simple! I will think of a number and you will try to guess it.")
#statement to generate a random no. btn 1 and 10 using randit()
number=random.randint(1,10)
isGuessRight=False
while isGuessRight != True:
    guess=input("Guess a nummber between 1-10:\n")
    if int(guess)==number:
        print("You guessed {}. You win. Congratlations!!!".format(guess))
        isGuessRight=True
    else:
        print("You guessed {}. Sorry try again".format(guess))'''
        
        
        
#For Loop

#Writing For Loop
print("Count to 10")
for x in range (0,100):
    print(x)