import math
dist=int(input("Enter the distance: "))
banana=int(input("Enter the number of bananas: "))
ip1=banana-dist
trip1=(2*(ip1/dist))+1
ip2=banana-ip1
trip2=(2*(ip2/dist))+1
x=math.ceil((banana-ip1)/trip1)
y=math.ceil((ip1-ip2)/trip2)
z=math.ceil(dist-x-y)
left=ip2-z
print(str(left) + " is the number of bananas remaining")
