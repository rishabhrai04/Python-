a = (1,2,5,6,False,"Rohan","Ravi", 3.14, 5.6, 7.8)
print(a) # <class 'tuple'>
no = a.count(2) # count the number of times 2 appears in the tuple
print(no) # 1
i=a.index(3.14)# index of 3.14 in the tuple
print(i) # 1


tuple1 = (1,2,3,)
tuple2 = (4,5,6,)
concatenated = tuple1 + tuple2 # concatenate two tuples
print(concatenated) # (1, 2, 3, 4, 5, 6)

my_tuple = (1, 2, 3)
repeated = my_tuple * 3 # repeat the tuple 3 times
print(repeated) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

my_tuple = (1, 2, 3) #Membership tuple
print(2 in my_tuple) # True
print(4 in my_tuple) # False

my_tuple = (1, 3, 2 , 4) # Length tuple
print(len(my_tuple)) # 4
print(max(my_tuple)) # 4
print(min(my_tuple)) # 1
print(sum(my_tuple)) # 10
print(sorted(my_tuple)) # [1, 2, 3, 4]



my_tuple = (1, 2, 3, 4, 5) # Slicing tuple
print(my_tuple[1:4]) # (2, 3, 4)
print(my_tuple[:3]) # (1, 2, 3)
print(my_tuple[3:]) # (4, 5)
print(my_tuple[-1]) # 5
print(my_tuple[-3:-1]) # (3, 4)
print(my_tuple[::2]) # (1, 3, 5)
print(my_tuple[::-1]) # (5, 4, 3, 2, 1)
print(my_tuple[1:4:2]) # (2, 4)
print(my_tuple[::3]) # (1, 4)
print(my_tuple[1:5:3]) # (2, 5)
print(my_tuple[1:5:-3]) # ()
print(my_tuple[1:5:-2]) # ()

print(my_tuple[1:5:1]) # (2, 3, 4, 5)
print(my_tuple[1:5:2]) # (2, 4)
print(my_tuple[1:5:3]) # (2, 5)



my_tuple = (1, 2, 3, 4, 5) # Tuple with different data types
print(type(my_tuple)) # <class 'tuple'>
print(type(my_tuple[0])) # <class 'int'>
print(type(my_tuple[1])) # <class 'int'>



my_tuple =(1,2,3) #Ucnpacking tuple
a,b,c = my_tuple # unpacking tuple into variables
print(a,b,c) # 1




