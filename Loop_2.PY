# i=0

# for i in range(3):
#     print(i)
# i= 0
# while(i<=3):
#     print(i)
#     i=i+1

# #input from user in loop
# while(i<40):
#     i=int(input("Enter the number: "))
#     print(i)
# else:
#     print("I'm inside else")

# print("Done with loop")

# #Decreasing loop
# count=6
# while(count>0):
#     print(count)
#     count=count-1
# else:
#     print("I'm inside else")
#infinity loop
# count= 5
# while(count>0):
#   print(count)
#   count= count + 1

#This is day 19 task
for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=",5*(i+1))
print("Outside the loop")
#This is continue statement
for i in range(12):
    if(i==10):
        print("Skip the line")
        continue
    print("5 X",i+1,"=",5*(i+1))
    
#This is while loop statement
i = 0
while True:
    print(i)
    i=i+1
    if(i%100 == 0):
        break