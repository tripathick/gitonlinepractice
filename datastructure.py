
# SET IN PYTHON.............
#.............................................
a=set()
a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))   #intersection of set value
print(a.union(b))       #Union of set value
print(a-b)

for i in a:   #Iterate the value of set
	print(i)

a={1,2,3,4,1,2,3,4} #In set only unique value is stored in a set.
print(a)

print(len(a))   #length of set

print(list(set(a)))	#convert set into list



#DICTIONARY IN PYTHON.....................................................................................................................
#.............................................................................................................................


a=[1,2,3,4]
print(a[0],a[1])

a={'name':["jatin",'CHANDAN ','KUNDAN','TRIPATHI'],
    'marks':'90',
    'subject':['English','Math','hindi'],
    'Friends':{'pulkit':'android','chandan':'iphone'}
    }
print(a['Friends'])   

for key in a:     #Iteration of dictionary element.
    print(key)
#SOME IMPORTANT DICTIONARY METHOD.........
for key,value in a.items():
	print(key,"=>",value)
for key in a.keys():
	print(key)
for val in a.values():
    print(val)	

print('hello important and charming person',a['name'])


print(a.clear())


#TUPLE IN PYTHON ................................................................................................................
#...............................................................................................................................
a=[1,2,3,4,5]
print(a[0])
print(id(a))
a[0]=5
print(a)
print(id(a))
a=(1,2,3,4,5)
print(a[0])

def func(*args):
	print(args)
func(1,2,3,4)

#swapping of two numbers
a=5
b=9
a=a^b	
b=a^b
a=a^b

print("value of a :",a,"value of b :",b)