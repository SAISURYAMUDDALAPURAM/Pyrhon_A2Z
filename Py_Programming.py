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



