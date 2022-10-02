n = int(input("Enter the number from 1 to 9 \n"))
p = 1
if 1 <= n <= 9 :   
    for j in range(n, 0, -1):
        k = 0
        for i in range(j, 0, -1):
            print(i, end = ' ')              
        print("") 
        while k < p:
            print(end = '  ')   
            k += 1
        p+= 1
else :
    print("The number doesn't satisfies limits!!!")

"""
get = 50
spend = 80
duty = 0
totalduty = 0
for i in range(1, 10):
    duty = spend - get
    totalduty += duty
    spend += spend / 50
print("Total duty for 10 months is: {0:.2f}".format(totalduty))



a = int(input("Enter a "))
b = int(input("Enter b "))
x = 0
if 1 < a < 100 and 1 < b < 100:
    if a > b:
        x = 2 * a / b + 1
    elif a == b:
        x = -445    
    elif a < b:
        x = (b + 5 )/ a
    print("Answer: ", x)
else :
    print("A or b is not valid!!!")"""

   
