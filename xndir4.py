#xndir_4 (Write a Python program to find intersection of two given arrays using Lambda.)
list_1 = set([1,2,3,4,5,6,7,8,9,10])
list_2 = set([1,3,4,6,7,9,10])
intersection = lambda a,b:a & b
print(intersection(list_1,list_2))