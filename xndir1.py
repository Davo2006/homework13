#xndir_1 (Write a Python program to square and cube every number in a given list of integers using Lambda)
x = [1,2,3,4,5]
square = list(map(lambda a:a*a,x))
cube = list(map(lambda a:a**3,x))
print(square,cube)




