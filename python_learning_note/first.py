

'''
first pyhton


print('hello world')
'''







#second python 

'''
a='hello world'
print(a.count('l'))
''' 

'''
a='hello world'
a=a.replace('world','jie')
print(a)


fn='jie'
ln='wang'
whole_name=f'{fn},{ln}. Welcome!'
#whole_name='{}, {}. Welcome!'.format(fn,ln)
print(whole_name)

'''





#third class
'''
a=3.1415926535898
print(type(a))
print(a/2)
print(a//2)
print(3%2)
print(round(3.75,1)) #one decimal
num1=3
num2=2
print(num1 == num2)
print(num1>num2)

num1=int('100')
num2=int('200')

print(num1+num2)

'''




#forth class
'''
couses=['math','history','phsic','computerscience']

print(couses[0])#如果不知道一共多少个element，用【-1】
print(couses[0:2])#第一个到第二个元素
couses.append('art')
print(couses)
couses.insert(0,'happy')
print(couses)
couses1=['1','2']
couses.insert(0,couses1)
print(couses)


couses.extend(couses1)
print(couses)#['1', '2'], 'happy', 'math', 'history', 'phsic', 'computerscience', 'art', '1', '2']
couses.pop()
print(couses)
couses.reverse()
print(couses)
couses.pop()
print(couses)
couses.sort()
print(couses)

new_course=sorted(couses)
print(new_course)
num=[1,12,13,56,100,54]
'''

'''
print(min(num))
print(couses.index('math'))
print('math' in couses)#check if math in list
for item in couses:
	print(item)

for index,couses in enumerate(couses,start=1):
	print(index,couses)
	
couses_str='-------'.join(couses)
print(couses_str)
new_list=couses_str.split('---')
print(new_list)


list1=['1','2','3','5']
list2=list1
print(list1)
print(list2)
list1[0]='10'
print(list1)
print(list2)



cs_couses={'history','math','physic','happy'}
art={'history','art','physic','happy'}

print(cs_couses.intersection(art))
print(cs_couses.difference(art))


empty_list=[]
empty_list=list()
'''






'''fifth class set

student ={'name':'jie','age':'21','courses':'math'}

print(student['courses'])#some key in dictionary

student['phone']='3.3.3.3.3'
student['name']='jam'

#print(student.get('phone','not foundbla'))
#print(student)    output: {'name': 'jam', 'age': '21', 'courses': 'math', 'phone': '3.3.3.3.3'}


student.update({'name':'wang','age':222})
print(student)
del student['name']# how to use delete
print(student)

print(student.keys())
print(student.items())
 #output dict_keys(['name', 'age', 'courses'])
         #dict_items([('name', 'jie'), ('age', '21'), ('courses', 'math')])

for key,value in student.items():
	print(key,value)

'''


'''sixth class condition

language='cpp'
if language =='cpp':
	print('language is cpp')
elif language =='python':
	print('language is python')
else:
	print('no match')


user='admin'
login=False

if user=='admin' and login:
	print('admin page')
else :
	print('bad ')
	
if not login:
	print('please log in again')
else:
	print('welcome')


condition = True

if condition:
	print("that's true")
else:
	print("that's false")

'''







''' seventh class loop

nums=[1,2,3,4,5]
for num in nums:
	if num==3:
		print('find it')
		break
	print(num)
output:
1
2
find it

nums=[1,12,5,12,3,5]
for num in nums:
	for letter in 'abc':
		print(num,letter)


x=0
while x<10:
	if x==5:
		break
	print(x)
	x+=1
	'''






'''eighth class function

def hello_func():
	print("hello")


hello_func()
hello_func()
#print(hf())
#print(len('test'))
#print(hf().upper()) #upper level


def hf(greeting,name):
	return '{}hello,{}'.format(greeting,name)


#print(hf('hi','jie'))

def student_info(*args,**kwargs):
	print(args)#tuple 
	print(kwargs)#dictionary

student=['math','art']
info={'name':'jie','age':121212}
student_info(*student,**info)



#瑞年计算
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def leap(year):
	return ((year%4==0) and (year%100!=0 or year%400==0))
def dayandmonth(year,month):
	if month in (1,12):
		return 'what the fuck are you typing, my buddy?'
	if month ==2 and leap(year):
		return 29
	return month_days[month]

print(leap(2020))

'''







#ninth class import Modules and the standard library

print('hello')
test='test string'
def find(to_search,target):
	for i,value in enumerate(to_search):
		if value == target:
			return i
	return -1

	










































