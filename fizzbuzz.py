#XTREME OPTIMIZAYSHUN
try:
    x = int(input("Enter a number: "))
except:
    print("Enter a number")
for i in range(x+1):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    elif output == "":
        output = i
    print(output)