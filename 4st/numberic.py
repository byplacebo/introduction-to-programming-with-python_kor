area = 0
width = 20
height = 10

#calculate the area of a triangle
area = width * height / 2

print("the area of the triangle would be %d" % area)
print("the area of the triangle would be %6d" % area)
print("the area of the triangle would be %06d" % area)
print("the area of the triangle would be %f" % area)
print("the area of the triangle would be %.2f" % area)

#printing the formatted decimal number with right justified to take up 6 spaces
#with leading zero
print("My favorite number is %06d !" % 42)
print("My favorite number is {0:06d} !".format(42))

#do the same thing with the .format syntax to include numbers out output
print("the area of the triangle would be {0:f} ".format(area))
print("My favorite number is {0:d} !".format(42))

#this is an example with multiple nubers
#I have use the \ to indicate command continues on next line
print("Here are three numbers! " + \
	"The first is {0:d} The second is {1:4} and {2:d}".format(7,8,9))
