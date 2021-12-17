x = 0
if(x==4):
    print("Aqib")
elif(x == 0):
    print("Shivam")
else:
    print("Suraj")

#-------------------------------------------------------


x=5

if x%2==0:
    print("e")
else:
    print("o")
    
#------------------------------------------------------

# for

for var in range(10,0,-1):
    print(var)
    
#---------------------------------------------------------

print([1,2,3,4,5,5,67,90, "hi", 7.8])



arr = [1,21,32,23,43,34,54,45]
print(arr[0])
print(arr[-1])


# Slicing

print(arr[0:4])

print(arr[0:7:2])

# iteration

a=[]
for i in arr:
    a.append(i**2)
print(a)
    
    
#----------------------------
arr = [1,21,32,23,43,34,54,45]
arr.append(000)
print(arr)

arr.insert(0, 999)
print(arr)
#---------------------------

e = arr.pop(5)
print(e)


a = 10
print(a/3)
print(a//3)


def su():
    print("Shivam")
def fun():
    print("Suraj")
    return 
    su()
fun()
print()
i="*"
for row in range(1,5):
    for col in range (row):
        print(i, end="")
    print()




