#Activity 1
myList1=[]
print("enter objests of first list...")
for i in range(5):
    val=input("enter a value:")
    n=int(val)
    myList1.append(n)

myList2=[]
print("enter objests of second list...")
for i in range(5):
    val=input("enter a value:")
    n=int(val)
    myList2.append(n)

list3=myList1+myList2;
print(list3)

#Activity2
def isPalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False

print(isPalindrome("deed"))

#Activity3
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
c = []
for indrow in range (3):
    c.append ([])
    for indcol in range(3):
        c[indrow].append (0)
        for indaux in range(3):
            c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]

print (c)

#Activity4
def perimeter(listing) :
    leng=len(listing)
    perimeter=0;
    for i in range(0,leng-1):
        dist = (((listing[i][0]-listing[i+1][0])**2)+
                 ((listing[i][1]-listing[i+1][1])**2))**0.5
        perimeter = perimeter + dist
    perimeter = perimeter + (((listing[0][0]-listing[leng-1][0])**2)
                             +((listing[0][1]-listing[leng-1][1])**2))**0.5
    return perimeter

L = [(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))

#Activity5
def symmDiff(a,b):
    e = set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e

set1={0,1,2,4,5}
set2={4,5,7,8,9}
print(symmDiff(set1,set2))


#Activity6
sample={("sohaib","ali"):"0246585468445", ("aib","li"):"02465854645",
        ("sib","ai"):"0246585468445",}
firstName = input("enter first name")
lastName = input("enter the last name")
                  
searchTuple = (firstName,lastName)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("name not found")

