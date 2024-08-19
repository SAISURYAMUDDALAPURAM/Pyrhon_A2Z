"""
Python: Very Easy to Learn, Simple English Based Programming Language
English : Grammer - In Speaking Language 
Python  : Syntax  - In Programming Language (Due to  Free source & more Modulesvery easy and powerful and general purpose language)

Python Full Stack:
1)Core Python 
2)Advanced Python
3)Python Modules (CapStoneProj: Python Modules Project)
4)UI (HTML,CSS,BS,JS,jQuery)
5)MySQL
6)Django & Flask (CapStoneProj: Python Full Stack Project)

Features:
1)Python is simple(syntax),easy(learning) and Powerful(Modules) 
2)Python is General Purpose Lang
3)Python Free & Open Source
4)Python is portable Language
5)Python is high level language
6)Python supports all databases(MySQL,MongoDB,SQLServer(.net),Postgresql,Oracle(java))
7)Python is expressive language (we only think of logic not syntax)
8)Python is Beginers language
9)Python is Interpreter Language(Interpreter executes Line by Line-MoreTime(But compiler executes all at a time -LessTime))
10)Python is Object Oriented Language
11)Python is strong and dynamically typed language

PIP(Python Package Installer)
"""
#Core Python
#1 KEYWORDS(35)  - Case Sensitive (True False None )These are Predefined words / Reserved words which has default functionality that cannot be changed, and we cannot use these as variables
#2 QUOTES        - single (') and double (") quotes, These are used to write String Values - Set of Characters within quotes is String, else Variable. (' & ") ->Single line string, (''' or """)-> Multiple line strings
#3 COMMENTS      - Gives more readability of program. 2 types Single Line-> # and Multiple Lines-> ''' or """ (without assigning)
#4 IDENTIFIER    - Used to Identify an Object (Variable names, Fun Names, Classes Name, List Name) Lower case,Uppercase,underscore and digits without spaces in between and No Pyhton keywords should be used , First letter should not be NUMBER, NO Special Characters allowed
#5 CASE STYLES   - lowercase,UPPERCASE,PascalCase(CLASSES & ARRAYS),camelCase (FUN & VAR),snake_case (FUN & VAR),kebab-case(kebab is not supported in python)
#6 VARIABLE      - Resserved Memory Location to Store User data ->if we have data ("Sai Surya") to save in memory -> We should have account in bank -> through vairbale name we can store user value and Each account has unique account number so each memory has Unique Memory Location ID
#7 DATA TYPES    - 1)Integer-int 2)Float-float 3)Bool- bool 4)complex-complex 2+3j 5)string-str
#8 ASSIGNMENTS   - a) 1:1 b) M:M c)M:1 d)1:M
name="Sai Surya"                                          #Assigning one value to one variable
name,loc,email = "Sai","Banglore","xyz@gmail.com"         #Assigning Multiple Values to Multiple Names
data="Sai","Banglore","xyz@gmail.com"                     #Assigning Multiple Values to one variable (automatically tuple)
studied_loc = fav_location = staying_loc = "Bengaluru"    #Assigning one value to Multiple variables 
#9 VARIABLE FUN  - print(variable)-> value of var,type(variable)->type of var,id(variable)-> address of var (if one data is stored then the same address is given to diffrent variables if same data)
#10 READ USERDATA - input() -> input function is used to read data from user <DEFAULT : Reads data in String Type>
#11 TYPECASTING FUN -  int(),float(),bool(),complex(),str(),eval()-> removes quotes
#NOTE: Addition Between numbers Concatination: Between Strings
#OPERATORS        - a+b - a,b are Operands + operator -> A symbol which perform operation on Operands
#OPERATOR TYPES   - 1)aritthematic +-*%/**exponenent //floor division 2)assignment = += -= *= //= **= 3)comparision/ relational == != >= <= < > 4)membership  in , not in5)identity is is not (to check the type of var) 6)logical not or and 7)bitwise | & ^ << >>

#DATA STRUCTURES   - Advanced DataTypes/Sequences/Collections 1)String 2) List 3)Dictionary 4)Tuple 5)Set (DS-Whcih allows set of data) 2 operations 1)Creating & 2)fetching DATA from Obejct -> we can fetch by 2 types 1) Indexing(Forward & Backward Indexing) - One element at a time 2) Slicing- fetching set of elements

#DS STRING TOPICS: 1)INDEXING 2)SLICING 3)CONCATNATION 4)REPEATATION 5)PACKING 6)UNPACKING 8)FUNCTIONS 9)IMMUTABILITY 10) ITEM ASSIGNMENT(no supports) 11)ITEM DELETION(not supports)
#INDEXING     - fetching specific character by its Index Number SLICING  - fetchig set of characters by using Start and end Index Numbers(1) str[startnum:endnum] 2) str[startnum:endnum:increment_num])
#PACKING AND UNPACKING - PACKING: 1) a+b+c 2) join(arg) - join([a,b,c]) UNPACKING: 1)NoOf New Variables = Nof Characters 
#STRING FUNCTIONS: 1)len(len of string) 2)count(count noof occurances) 3)index(find the index of value) 4)lower(lowercase all) 5)upper(uppercase all) 6)swapcase(reverse the case of fun) 7)islower(to check all in lower True/False) 8)isupper(To check all uppercase True/False) 9)capitalize(in entire string firts character upper) 10)title(Each first character in word) 11)startswith(string starts with) 12)endswith() 13)replace('charcter','replcing value',no of characters to change) 14)split(',') -> gives output in list & default is space 15) strip() 16)lstrip() 17)rstrip
st='***Python***'
print(st.strip('*')) #output: 'Python'
print(st.lstrip('*')) #output: 'Python***'
print(st.rstrip('*')) #output: '***Python'
st='*!*!*Python*!*!*'
print(st.lstrip('*')) #output: '!*!*Python*!*!*'
print(st.rstrip('*')) #output: '*!*!*Python*!*!'
st1='python full stack'
print(splt()) #output: ['python','full','stack']
print(splt(' ')) #output: ['python','full','stack']
print(splt(n)) #output: ['pytho',' full stack']

#DS LIST TOPICS: 1)INDEXING 2)SLICING 3)CONCATNATION 4)REPEATATION 5)PACKING 6)UNPACKING 8)FUNCTIONS 9)MUTABILITY 10) ITEM ASSIGNMENT 11)ITEM DELETION 12) created by using [],list(),range()
#LIST FUNCTIONS : 1)len() 2)count() 3)index() 4)max() 5)min() 6)sum() 7)all(all must be non zero values in list 0 and False) 8)any(any one in list not zero) 8) to add new data in list append() 9)extend() 10)insert(index,element) 11)remove(targets first element) 12)pop(targets index and removes , pop removes last index will go) 13)clear(all list to empty) 14)del(delete can be used to del entire list and each element also)
#NESTED LIST: 
lst1=[10,20]
lst2=[a,b]
lst3=[True,False]
lst=[lst1,lst2,lst3]
print(lst) #output: [[10,20],[a,b],[True,False]]

#DS TUPLE TOPICS: 1)INDEXING 2)SLICING 3)CONCATNATION 4)REPEATATION 5)PACKING 6)UNPACKING 8)FUNCTIONS 9)IMMUTABILITY 10) ITEM ASSIGNMENT(no supports) 11)ITEM DELETION (no supports) 12) created by using [],list(),range()
#TUPLE can be created by using 1) () 2) without using () 3)tuple() , Tuple doesnot allow ADDING & item DELETION FUNCTIONS (its static) allows -> del tuple_var - Tuple is immutable form of LIST

#DS SET TOPICS: (NORMAL SET(LIST),FROZEN SET(TUPLE))Created by using 1){ } 2)set(), Diffrent from String , List, Tuple (will not allow duplicates and Order will change no indexing of elements), set not support indexing and slicing , support packing and unapcaking , set is mutable object
#SET SPECIAL FUNCTIONS: 1) union() 2)intersection() 3)difference() 4)symmetric_difference() 5)intersection_update() 6) difference_update() 7)symmetric_difference_update() 8) discard()
#SET TYPES: Normal set & Frozen Set #f=frozenset([10,20,10,20,30,30])

#DS DICTIONARIES TOPICS: Collection of Key:Value Pairs , no key duplicates should be there
#CALL OPERATIONS ON DICTINOARIES: C U R D operations 1) Create: Creating /Adding new pairs to existing dict 2) Update: Modifythe Values of keys 3)Retrieve : Display values of keys 4) Delete: Deleting exidting dict / deleting existing key value pairs 5)pop(if no arguments gives error) 6)popitem(last item by default - not allows key) 7)keys() 8)values() 9) items(key value pair comes as tuple) 10)update()
#NESTED DICTIONARY : data={student1:{'name':'sai','age':10}},student2:{'name':'surya','age':15}}

#CONTROL STATEMENTS : 1) CONDITIONAL STATEMENTS 2)ITERATIVE STATEMENTS 3)TRANSFER STATEMENTS
#CONDITIONAL STATEMENTS : Control the flow of Program execution 1)Simple If 2) if-else statement 3)elif statement 4) nested if statemwnt
#ITERATIVE STATEMENTS :  1) FOR LOOP 2) WHILE LOOP
#TRANSFER STATEMENTS :  1) BREAK 2) CONTINUE 3) PASS 

#FORMAT SPECIFYERS : x=10 ;  print('{} this flower bracket is placeholder'.format(x))
#range() : range(startnum,endnumber,increment), range(startnum,endnumber), range(endnumber)
#FUNCTIONS: Set of Reusable statements which are used to perform specific task
"""
def maxOfTwoNums(a,b): #def -> defining function maxOfTwoNums-> function deifination a,b->(formal / positional) decide by developer argumnets , we can have default arguments by developer while develping fun
  if a>b:
    print(a)
  else:
    print(b)

maxOfTwoNums(10,20) #maxOfTwoNums -> function call #10,20-> actual arguments (fixed length argumnets) (variable length arguments)  if maxOfTwoNums(b=20,a=10) is called keyword argumentif we use formal arguments in funcall toassign the actual value then
"""
#when actual value is there default value is ignored actual value is taken
"""
def display(a,b=10):
    print(a)
    print(b)
display(20,1000)
"""
#Fixed length Non Keyword Arguments
"""
def fun(a,b):
 print(a)
 print(b)
fun(1,2)
"""
#Fixed Length keyword Arguments 
"""
def fun(a,b):
 print(a)
 print(b)
fun(a=11,b=22)
"""
#Variale Length Non Keyword Arguments
"""
def fun(a,b,*c):     ##### *c= *args
 print(a)
 print(b)
 print(c) #gives tuple
fun(11,22,33,44,55,66)
output: 11, 22, (33,44,55,66)
"""
#Variable Length Keyword Arguments
"""
def fun(a,b,*c,**d):     ##### *c= *args    **d=**kwargs
 print(a)
 print(b)
 print(c) #gives tuple
 print(d) #gives dict
fun(11,22,33,44,55,66,x=10,y=20,z=30)
output: 11, 22, (33,44,55,66), {'x':10,'y':20,'z':30}
"""
#COMPREHENSIONS: Compreshensions is an advance level of writing programs 
#SYNTAX: < expression > <for loop > <if condition >

#Find Vowels or not 
#print(i for i in st if i in 'aeiou')
#Odd num
#print([i for i in num if i%2!=0])
"""
print([i for i in strt_vowel.split() if i[0] in 'aeiouAEIOU']) #list
print(tuple(i for i in strt_vowel.split() if i[0] in 'aeiouAEIOU')) #tuple
print({i for i in strt_vowel.split() if i[0] in 'aeiouAEIOU'})#set
"""
#print(i,end='\n')
"""
LAMBDA EXPRESSIONS/FUNCTIONS:
Nameless Functions/ Ananymus Functions / use and Throw functions

syntax: 
lambda <arg_list> : <expressions>
"""
"""
function to add two numbers

#  def addition(a,b):
    c=a+b
    print(c)
 addition(10,20)

#x=lambda a,b: a+b
print(x(10,20))
"""
# FILTER function  - TO filter the data
"""
it is a FOR loop you can filter the entire valid values for condition

#even number program
lst=[10,20,30,1]
print(list(filter(lambda i: i%2==0,lst)))
"""
"""
#MAP - to apply same logic for all the elements

#print(list(map(lambda i:i+10,lst)))
#list(map(int, input().split())) -> while taking inputs 
# print([i**2 for i in lst])
#print(list(map(lambda i: i**2,lst)))

#REDUCE - reduce function is part of "functools" modules
#all elements in list if reduced to one functionality is called reduce 
#ex: if highest number in list 
#ex: if lowest number in list
#ex: sum of elements in list

(lambda a,b: a if a>b else b,lst)-> its gemeral but for list 

import functools as f
print(f.reduce(lambda a,b: a if a>b else b,lst))
max(lst)
import functools as f
print(f.reduce(lambda a,b: a if a>b else b,lst))
min(lst)
import functools as f
print(f.reduce(lambda a,b: a+b,lst))
sum(lst)
"""

"""
File handling / File I/O Operations
Py file       Text file
1)Input /add/write DATA - Adding data to file/writing data to file
2)Output / Fetch/ read DATA - getting data / reading data from file

RULES:
1. Open file
2. Write the data 
3. close the file 


Syntax:
open('filename.txt-> if file path is not specified by default it goes and search in folder where python is installed','mode of operation')

if not specify path 
interpreter goes to path and find file is it not find it will create on with that file and it will open it 

a=open('oursai.txt','w')
a.write('Hello Studnts')
a.close()

a=open('oursai.txt','a') - append on it will append at end

a.write('Hello Studnts alll')
a.close()

cusor stand at end of data is called FILE POINTER
#WRITE
a=open('dummy.txt','w')
a.write("sai\nHello World,\nSai Surya")
a.close()

a=open('C:\\Users\\smuddala\\Desktop\\Process_Improvement_Project\\new.txt','w')
a.write("sai")
a.close()

#READ
a=open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r')
#b=a.read()
#c=a.readline()
#d=a.read(3)
e=a.readline(2)
#print(b)
#print(c)
#print(d)
print(e)
"""
"""
##a=open('dummy.txt','w')
##a.write("sai\nHello World,\nSai Surya\n Here are we with File IO operations\n file is filled")
##a.close()

#a=open('C:\\Users\\smuddala\\Desktop\\Process_Improvement_Project\\new.txt','w')
#a.write("sai")
#a.close()
##a=open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r')
##b=a.read()
##print(b)
##print(type(b))
#b=a.read()
#c=a.readline()
#d=a.read(3)
#e=a.readline(2)
#print(b)
#print(c)
#print(d)
#print(e)
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').read())
print(len(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').read()))
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines()[-1])
print('_____________________________________________________________________')
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines()[1])

print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines()[2].split(',')[1][0])

print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines()[-1].split(',')[-1][-1])

print([i for i in open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').read().replace('\n',',').split(',') if i[0].upper()=='S'])


print([i for i in open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').read().replace('\n',',').split(',') if i[-1].lower() in 'aeiou'])

print([i.split(',')[0] for i in open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines()])
print("######################################################################")
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').read())
print("######################################################################")
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readline())
print("######################################################################")
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines())
print("######################################################################")
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').read(3))
print("######################################################################")
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readline(3))
print("######################################################################")
print(open('C:\\Users\\smuddala\\Desktop\\PYTHON_TRIALS\\dummy.txt','r').readlines(1))
"""
"""
REGULAR EXPRESSIONS: RE is used to Write Patterns

Check Pattren of Mobile Number / Check the pattren of Email we will have RE program/ vehicle registration numbers / perfect password / valid password checker 

If we want to write pattrens we should know
1) Character Classes : 2 types
 -A) System Defined- (/s-trying to match space character) (/S-to match everything except space) (/d - to match digits(0-9) (/D- to match everything execpt digits))
                    (/w-trying to match word (lower case/upper case/digits,underscores) ) (/S-to match everything except word (special characters)) (. dot - to match word includeing special characters)
                    
 -B) User Defined - requirement - (only lower case match, only uppercase match , or only lower case a,b,c,d)
                [a-z] -> to match all lowercase characters
                [abcd]-> to match either a or b or c or d 
                [a-zA-z] -> to match lower and upper characters
                [^a-z]   -> to match everything excpet lower case characters
                [0-9]   -> to match all digits
                [a-zA-Z0-9]-> to match all lower upper and digit characters
                
2) Quantifiers : if you want to match 2 spaces / 3 spaces or / 
                  a   -> if we want to march a
                  a?  -> a will match 0 time or 1 times
                  a+  -> a will match 1 or more times
                  a*  -> a will match 0 times or 1 or more times
                  a{3} -> a will match exactly 3 times
                  a{2,3} -> a will min 2 times and max 3 times
                  a{3,}  -> a will match min 3 times and max no limit
                   
3) RE Functions:
          -A) match()
          -B) fullmatch()
          -C) search()
          -D) findall()
          -E) split()
          -F) sub() and subn()


import re
#name=input("Enter Any String: ")
#m=re.match("Py",name) #only tries to match at beginning of the string
#m=re.fullmatch("Py",name) #tries to match fully in string
#m=re.search("Py",name) #tries to match at entire sentacece

m=re.findall('[a-z]','Na1*Tm2@Hx3$')
m=re.findall('[^a-z]','Na1*Tm2@Hx3$')
m=re.findall('[a-zA-Z0-9]','Na1*Tm2@Hx3$')
m=re.findall('[^a-zA-Z0-9]','Na1*Tm2@Hx3$')
m=re.findall('\W','Na1*_ Tm2@H_x 3$')
m=re.findall('.','Na1*_ Tm2@H_x 3$')
#Substitute
m=re.sub('a','_','Sai Surya')#it replaces all 
m=re.subn('a','_','Sai Surya')#it replaces and it will give count of no of times sub
m=re.split(',','Nara,yana , Tech ,House')

print(m)
if m==None:
    print('No Matching')
else:
    print('Matching')
"""

