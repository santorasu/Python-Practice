def average(a,b):
    print("The average is ",(a+b)/2)

average(1,3)

def average(a=9,b=1):
    print("The average is ",(a+b)/2)

average(b=2)

def name(fname,mname="Rasu",Lname="Santo"):
    print("Hellow,",fname,mname,Lname)

name("Ami")

#Number of average
def average(*numbers):
    print(type(numbers))
    sum= 0
    for i in numbers:
        sum = sum + i
    #  print("Average is : ",sum/len(numbers))
    return sum /len(numbers)
c = average(5,6,7,1)
print(c)