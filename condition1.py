#conditions
#if condition by using comparision operator
#<,>,<=,>=,!=,==
'''a=4
b=8
if a<b:
    print("true")'''
    
'''a=4
b=8
if a>b:
    print("true")'''
'''a=5
b=10
if a<=b:
    print("less")'''

'''a=6
b=12
if a>=b:
    print("true")'''

'''a=4
b=8
if a!=b:
    print("true")'''

'''a=4
b=4
if a==b:
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a>30:
    print("false")'''

'''a="python"
if a=="python":
    print("true")'''

'''a=input("enter the name")
if a=="indu":
    print("true")'''

#if condition by using logical operator
#and,or,not
'''a=3
b=8
if a<b and b>a:
    print("true")'''

'''a=3
b=8
if a<=b and b>=a:
    print("true")'''

'''a=3
b=8
if a!=b and b==a:
    print("true")'''

'''a=5
b=10
if a<b or b>a:
    print("true")'''

'''a=3
b=8
if a<=b or b>=a:
    print("true")'''

'''a=7
b=11
if a!=b or b==a:
    print("true")'''

'''a=12
b=15
if not a<b:
    print("less")'''

'''a=12
b=15
if not a>b:
    print("less")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("less")'''

'''a=int(input("a value"))
if a!=9 or a==6:
    print("true")'''
    
'''a=input("enter the data")
if a=="python" or a=="java":
    print("true")'''

#if condition by using identify operator
#is,is not
'''a=8
if type(a) is int:
    print("it is int")'''

'''a=8
if type(a) is not int:
    print("it is int")'''

'''a=int(input("a value"))
if type(a) is int:
    print("true")'''
'''a=6.2
if type(a) is float:
    print("it is float")'''

'''a=6.2
if type(a) is not float:
    print("it is float")'''

'''a=float(input("a value"))
if type(a) is float:
    print("true")'''

#if condition by using membership operator
#in,not in
'''a=[2,3,4,5,6,7,8,9,10]
if 10 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 10 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 20 not in a:
    print("true")'''

'''a=int(input("a value"))
if 10 in a:
    print("true")''' #error

'''a=[10,20,30,40,50]
b=int(input("value"))
if b in a:
    print("true")'''
