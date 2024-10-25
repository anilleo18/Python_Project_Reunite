mylist = ["Anil", "zebra", "lion", "cat"]
for x in mylist:
    print(x)

for x in range(0, len(mylist)):
    print(mylist[x])

rev = ""
print(sorted(mylist))

mylist2 = []
count = 0

for x in mylist:
    mylist2.append(x[::-1])

print(mylist2)

rev = ""

for x in range(0, len(mylist)):
    for y in range(len(mylist[x]) - 1, -1, -1):
        rev = rev + mylist[x][y]
    mylist2.append(rev)
################################ NOTES ###############################
mylist: list = []
print(mylist)
print(type(mylist))

# mylist_1: list = eval(input("Please enter your list 2 :"))
# print(mylist_1)
# print(type(mylist_1))

# mylist_3: list = eval(input("please enter the list 3:"))
# print(mylist_3)
# print(type(mylist_3))

sentence = 'Algebra Geomentry'
mylist = list(sentence)
print(mylist)

print(ord('a'))
print(ord('A'))
print(ord('#'))

word = 'hey hello how are you doing!!!'
mylist2 = word.split()
print(mylist2)

wordList = ['a', 'b', 'c', 'd', 'e']
print(wordList[0])
print(wordList[len(wordList) - 1])
print(wordList[-1])
print(wordList[0:60:2])
print(wordList[-1:-7:-1])

alpha = "ANIMAL"
print(alpha[0:30:2])
print(alpha[-1:-4])

wordList = ['a', 'b', 'c', 'd', 'e']
print(wordList[2:20])

mylist = [10, 20, 30, 40, 50]
print(mylist)

mylist[2] = 300
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']

for x in range(0, len(mylist)):
    print(mylist[x])

count = 0
while count < len(mylist):
    print(mylist[count])
    count += 1

numberlist = [1, 2, 3, 3, 4, 5, 66, 7, 7, 88, 8]

count = 0
while count < len(numberlist):
    if numberlist[count] % 2 == 0:
        print(numberlist[count], end=' ')
    count += 1

for n in numberlist:
    if n % 2 == 0:
        print(n, end=' ')

number_list = [11, 20, 30, 35, 40, 5, 66, 7, 7, 88, 8]

alpha = "heyanilhow"
res = ':'.join(alpha)
print(res)

lister = ['monkey', 'Donkey', 'Banana']
res = " ".join(lister)
print(res)

for x in range(0, len(numberlist)):
    print('Negative index', x - len(numberlist), " positive index ", x, 'of value', numberlist[x])

print(len(number_list))
print(number_list.count(7))
print(number_list.index(8))

mylist: list = []

for x in range(1, 101):
    if x % 10 == 0:
        mylist.append(x)

print(mylist)

list_ins = [10, 20, 30, 40, 50]
list_ins.insert(-2, 900)
print(list_ins)

mylist = [1, 3, 4, 5, 6, 67, 7, 7787, 5, 5, 5]
mydict = {}

for x in mylist:
    if x in mydict:
        mydict[x] = mydict[x] + 1
    else:
        mydict[x] = 1
maxcount = 0
maxval = ""
for key, value in mydict.items():
    print(key, "  ", value)
    if value > maxcount:
        maxcount = value
        maxval = key

print(maxval, '...', maxcount)
temp = 0

for x in range(0, len(mylist)):
    for y in range(x + 1, len(mylist)):
        if mylist[x] > mylist[y]:
            temp = mylist[x]
            mylist[x] = mylist[y]
            mylist[y] = temp
print(mylist)

mylist = [1, 3, 45, 98, 200]
count = 0
for x in mylist:
    count = count + x
print(count)

# Largest Number:
mylist = [11, 3, 4335, 98, 2, 200]

Max_val = 0
for x in mylist:
    if x > Max_val:
        Max_val = x
print(Max_val)

Min_val = mylist[0]

for x in range(1, len(mylist)):
    if mylist[x] < Min_val:
        Min_val = mylist[x]

print(Min_val)

counter = 0
temp = 0

while counter < len(mylist):
    if mylist[counter] % 2 == 0:
        temp += 1
    counter += 1
print('no of even items: ', temp)

h_temp = 0
for x in range(0, len(mylist)):
    if mylist[x] % 2 == 0:
        h_temp += 1
print(h_temp)

mylist = [11, 3, 4335, 98, 2, 200]

game = 0
for x in range(0, len(mylist)):
    if x % 2 == 0:
        h_temp += 1
        mylist.insert(x, game)

print(mylist)

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['z', 'p', 'k']

mylist1.extend(mylist2)
print(mylist1)

mylist1.remove('k')
print(mylist1)

mylist1 = [1, 2, 3, 4, 5]
print(mylist1.pop())
print(mylist1.pop(1))


class BankAccount:
    _balance = 0

    def __init__(self, bal=0):
        self._balance = bal

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    @property
    def balance(self):
        return self._balance


my_account = BankAccount()
my_account.deposit(50)
ulti_balance = my_account.balance
print("ulit balance", ulti_balance)
