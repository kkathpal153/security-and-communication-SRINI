import math


prime_number = int (raw_input("enter the prime number : "))
primitive_root = int (raw_input("enter the primitive root : "))

xa = 6
xb = 8

print (" the private key of A is : " + str(xa) )

print (" the private key of A is : " + str(xb) )

i = int(math.pow(primitive_root,xa))  #secret key of sender A
j= int(math.pow(primitive_root,xb))   #secret key of receiver B

ya = i % prime_number
yb = j % prime_number
print ( " the public key of A ( ((p)^xa))mod g ) is " + str(ya))

print ( " the public key of B ( ((p)^xb))mod g ) is " + str(yb))

print ( "now they exchange the public key" )

i = int(math.pow(yb,xa))
ra = i % prime_number

j = int(math.pow(ya,xb))

rb = i % prime_number
print 
print ( " the value of computation after key exchange is is " + str(ra))

print ( " the value of computation after key exchange is " + str(rb))
