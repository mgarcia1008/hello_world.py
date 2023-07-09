#Print all intergers from 0 - 150
for i in range (0,151):
    print(i)

#print all multiples of 5 from 5 to 1000
for i in range (5,1001,5):
    print(i)

#print integers 1-100. If divisible by 5 print "coding" if divisible by 10 print coding dojo
for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else: 
        print(i)

#add odd integers from 0 to 500,000 and print final sum
sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)

#Print positive numbers starting at 2018 counting down by fours
for i in range (2018,0,-4):
    print(i)

#flexible counter 
lowNum = 2
highNum = 9
mult = 3
for i in range (lowNum,highNum + 1):
    if i % mult == 0:
        print(i)
