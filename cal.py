def add (P, Y):
    return P+Y
def substract (P, Y):
    return P -Y
def multiply (P, Y):
    return P * Y
def divide ( P,Y ):
    return P/Y
print("a.add")
print('b.substract')
print("c.multiply")
print('d.divide')
fish=input('Enter a,b,c or d')
no1=int(input("ENTER YOUR NO."))
no2=int(input('Enter your second no.'))
if fish == 'a':
    print(no1, '+', no2, '=', add (no1,no2))
elif fish == 'b':
    print(no1, '-', no2, '=', substract (no1,no2))
elif fish == 'c':
    print(no1, '*', no2, '=', multiply (no1,no2))
elif fish == 'd':
    print(no1, '/', no2, '=', divide (no1,no2))
else:
    print('Invalid')


