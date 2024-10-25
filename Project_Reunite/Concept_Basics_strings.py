import string

a = 30
b = 90
print(a + b)

s1 = ' anilleo'
ch = 'a'

for s in s1:
    print(s)

print(s1.strip())
print(s1.lstrip())
print(s1.split())
print(s1.lower())
print(s1.capitalize())
print(type(s1))
print(type(ch))

s2 = 'hi \' hello how are you'
s3 = '''hello how are "you" doing 'my' love '''
s4 = "hey \"why\" did you \'open\' door "

print(s2 + '==' + s3 + "==" + s4)

delta = 'sunnyvalley'
print(delta[0])
print(delta[1])
print(delta[-1])
i = 0

for val in delta:
    print("the positive index is {} and negative index is {} and value is ".format(i, i - len(delta), val))
    i = i + 1

postalcode = '522002'

for i in range(len(postalcode)):
    print(postalcode[i])

delta = "PorterhouseCoopers23"

for x in range(0, len(delta), 3):
    print(x)
    print(delta[x])

delta = 9
for i in range(0, 10):
    print(i, 9, i * 9)

delta = "hey your house number is23"

print(delta[0:3])
print(delta[-1:-5:-1])
print(delta[::-1])  # Reverse a string
print(delta[::])
delta = "Porterhouse python"
# print complete String
print(delta[:])


# tell a string is anagram

def alpha(frier):
    esther = frier[::-1]

    if frier == esther:
        print("give string  is anagram")
    else:
        print("give string is not a anagram")


alpha("abba")
alpha("tomato")

delta = " hey hello due "
print(delta.strip())
print(delta)

list_delta_val = delta.split(" ")
print(list_delta_val)
val = ''

for x in list_delta_val:
    val = val + x

print(val)

delta = "abcdefgh"
print(delta[-2:-5:-1])
print(delta[-2:-7:-2])

delta = "hello!!!"
print(delta + delta)
print(delta * 3)

delta = "Anil!"
n = -1

while n >= -len(delta):
    print(delta[n], end=' ')
    n = n - 1

delta = "Aanya"
n = 0
#########################################
while len(delta) > n:
    print(delta[n], end=' ')
    n = n + 1

x = -1
while x >= - len(delta):
    print(delta[x], end=' ')
    x = x - 1
########################################
for x in delta[::]:
    print(x, end='')
    print("  ")

for x in delta[::-1]:
    print(x, end='')
    print("  ")


def method_m1(delta, deltasub):
    if deltasub in delta:
        print("your sub is present")
    else:
        print("No you sub is not present")


method_m1("Ahlan wa marhaban iszmee anil wa3makhum jarzheen yella yella !!!", "yella")

delta = "anilleo18"
print('8' in delta)
print('l' in delta)
print('x' in delta)


def method_compare(a, b):
    if a == b:
        print("yes strings are equal:")
    else:
        print("string are not equal:")


# s1 = input("hell please enter string s1 :")
# s2 = input("hello please enter string s2")
method_compare("anil", "beta")

delta = "jaamadddddlal"
print(delta.find("hello"));
print(delta.find("maharani"))
print(delta.rfind("a"))
print(delta.rindex("a"))
print(delta.index("a"))

delta = "capital:pushbike"
print(delta.find(":", 5, 9))
print(delta.rindex("k"))

mainstring = "anil"
substring = "a"
pos = -1
flag = False

while True:
    if substring in mainstring:
        pos = mainstring.find(substring, pos + 1, len(mainstring))
        if pos == -1:
            flag = False
            break
        print("Sub string residing in index : ", pos)
        flag = True;
        pos = pos + 1
    else:
        flag = False
        print("no any substring present in main string ")
        break

###########################################
alpha = "capital:cYork side:cManchester:cDetroit"
print(alpha.count(":"))
print(alpha.count("c", 1, len(alpha)))
##########################################
alpha = "hello how are you "
print(alpha.replace("you", "iam"));
############################################
alpha = "aabababbababaababa"
print(alpha.replace("a", "b"))
############################################
s = "Anil"
s1 = s.replace("A", "b")
print(s1)
print(s)
print(id(s1))
print(id(s))
############################################

alpha = "capital of country is Delhi"
mylist = alpha.split()
rev = " "
n = -1
while n >= -len(mylist):
    print(mylist[n], end=' ')
    n = n - 1

alpha = "Africa is home of many"
mylist = alpha.split()
print("     ")

for i in range(-1, -len(mylist) - 1, -1):
    print(mylist[i], end=" ")

print("   ")

for i in range(0, len(mylist)):
    print(mylist[i], end=" ")

alpha = "india is home of large groups"
mylist = alpha.split();
rev = "  "
words = ""
print("    ")
for i in range(0, len(mylist)):
    word = mylist[i]
    rev = rev + word[::-1]

print(rev.strip())

alpha = "a1b2c3"
print(len(alpha))

for i in range(len(alpha)):
    print(alpha[i])

alpha = ["Monday", "doomsday", "wednesday", "thursday", "friday"]

for i in alpha:
    print(i, end=' ')

print("  ")
beta = []

for i in range(-1, -len(alpha) - 1, -1):
    print(alpha[i], end=' ')
    beta.append(alpha[i])

print("  ")
print(beta)

alpha = ["Monday", "doomsday", "wednesday", "thursday", "friday"]
delta = []
rev = " "

for i in range(len(alpha)):

    if i % 2 == 0:
        rev = alpha[i]
        delta.append(rev[::-1])
    else:
        delta.append(alpha[i])

print(delta)

alpha = "a1b2c3"
beta = ""
teta = " "

for i in range(len(alpha)):
    if alpha[i].isdigit():
        beta = beta + alpha[i]
    elif alpha[i].isalnum():
        teta = teta + alpha[i]

print(beta)
print(teta.strip())

beta = alpha.split("-")
for x in beta:
    print(x, end=" ")

alpha = "28-08-1996"
new_date = alpha.replace("1996", "1997")
print(new_date)

alpha = "hello how are you"
s1 = alpha.replace("how", "too")
print(s1)

alpha = "28-08-1996"
beta = alpha.replace("1996", "1997")
gamma = beta.split("-")

for x in gamma:
    hepta_new = "-".join(gamma)

print(hepta_new)

mytup = ("sunday", "monday", "tuesday")
mytup_new = "--".join(mytup)
print(mytup_new)

mylist = ["sunday", "Monday", "Tuesday"]

alpha = "AnilLeo19@GMAIL"
print(alpha.swapcase())
alpha = "AnilLeo19 GMAIL"
print(alpha.title())  # Every Word will be like this
alpha = "AnilLeo19 aGMAIL"  # only few words be like this
print(alpha.title())
print(alpha.capitalize())

alpha = "Capital of the world is London"
print(alpha.startswith("Capital"))
print(alpha.endswith("London"))

alpha = "26864"

if alpha.isalnum():
    print('Given items has all numbers and charecters')
    if alpha.isnumeric():
        print("given item is numeric")
        if alpha.isalpha():
            print("given item has only string")
            if alpha.isdigit():
                print("this is digit")

alpha = "1234"
if not alpha.isalpha():
    print("all are ok ")

alpha = "hello"
beta = "Bison"
gamma = "grounds"

print("hey {x} i am in {y} large {z}".format(x=alpha, y=beta, z=gamma))

## Concept Python solutions:

alpha = "anileo18"
n = -1
rev = ""

while n >= -len(alpha):
    rev = rev + alpha[n]
    n = n - 1

print(rev)

alpha = "anil"
rev2 = ""
for i in range(-1, -len(s) - 1, -1):
    rev2 = rev2 + alpha[i]
print(rev2)

alpha = "anilleo18"
oddposition = ""
evenposition = ""

for x in range(0, len(alpha), 2):
    print(alpha[x] + oddposition, end=' ')

for x in range(1, len(alpha), 2):
    print(alpha[x] + evenposition, end=' ')

alpha = "anil"
oddposition = ""
evenposition = ""
n = 0

while len(alpha) > n:
    if not n % 2 == 0:
        print(alpha[n], end=" ")

    n = n + 1

alpha = "anil"
beta = "kamal"
output = ""
n = 0
m = 0;

while len(alpha) > m or len(beta) > n:

    if len(alpha) > m:
        output = output + alpha[m]
        m = m + 1

    if len(beta) > n:
        output = output + beta[n]
        n = n + 1
print(output)

alpha = "a1m8k9s20"
s1 = s2 = ""
S1_output = s2_output = ""

for x in alpha:
    if x.isalpha():
        s1 = s1 + x
    elif x.isnumeric():
        s2 = s2 + x

print(sorted(s1))
print(sorted(s2))

for x in sorted(s1):
    S1_output = S1_output + x

for x in sorted(s2):
    s2_output = s2_output + x

print(S1_output)
print(s2_output)

alpha = "a4b5c2"
output = ''

for x in alpha:
    if x.isalpha():
        output = output + x
        reptition_of_char = x
    elif x.isnumeric():
        output = output + reptition_of_char * (int(x) - 1)

print("")
print(output)

print("   duplication killer")
alpha = "aaabbbahhhhcaaaacccc"
mylist = []

for x in alpha:
    if x not in mylist:
        mylist.append(x)

output = "".join(mylist)  ##Remember join will retreive all elements in List

print(output)

mydict = {"name": "anil", "city": "Ab", "country": "UEA"}

for k, v in mydict.items():
    print(k + "======" + v)

print(mydict["name"])

alpha = "aaabbabssbssbbb"
dict = {}
Max_count = 0
Max_char = ""
for x in alpha:
    if x in dict:
        dict[x] = dict[x] + 1
    else:
        dict[x] = 1

for key, value in dict.items():

    if value > Max_count:
        Max_char = key
        Max_count = value

print('Max char {} and Max Count {} '.format(Max_char, Max_count))

alpha = "Hellohowareyoudoing!!!!!!!!!"
mydict = {}
maxchar = ""
maxcount = 0

for x in alpha:
    if x in mydict:

        mydict[x] = mydict[x] + 1
    else:

        mydict[x] = 1

for key, value in mydict.items():

    if value > maxcount:
        maxcount = value
        maxchar = key

print("the most repetitive charecter is {} and repeated {}".format(maxchar, maxcount))

mylist = [2, 1, 3, 4, 2, 5, 33, 44, 22, 9]
temp = 0;
for x in range(0, len(mylist)):
    for y in range(x + 1, len(mylist)):
        if mylist[y] < mylist[x]:
            temp = mylist[y]
            mylist[y] = mylist[x]
            mylist[x] = temp

print(mylist)

strokes = "aabdjdbdjbbbbbb"
mydict = {}
count = 0

for x in strokes:

    if x in mydict:
        mydict[x] = mydict[x] + 1
    else:
        mydict[x] = 1
max_count = 0;
max_value = None;
for key, value in mydict.items():

    if max_count < value:
        max_count = value
        max_value = key
print(max_value, "----", max_count)

alpha = "HEXAGON"
count = 0

for x in range(0, len(alpha)):
    print(alpha[x])
    count = count + 1

print("number of letters in X :", count)

mylist = [[1, 2, 3, ], [20, 30], [100, 200, 500]]

for x in mylist:
    for num in x:
        if num == 500:
            print("yeah this List contains 500")

mylist = [[1, 2, 3], [20, 30], [100, 200, 500]]
mylist_2 = []

# Taking even numbers and adding into list

for x in mylist:
    for num in x:
        if num % 2 == 0:
            mylist_2.append(num)
print(mylist_2)

vowels = ['a', 'e', 'i', 'o', 'u']
word = "hell0howareyou"
mylist = []

for x in word:
    if x in vowels:
        if x not in mylist:
            mylist.append(x)

print("word contains", mylist)

vowels = ['a', 'e', 'i', 'o', 'u']

for x in range(0, len(vowels)):
    print('{m} and {n} of letter {p}'.format(m=x, n=x - len(s) - 1, p=vowels[x]))

mydict = {"aanya": "daugther", "jaya": "mother", "navya": "wife"}
print(mydict["navya"])
print(mydict.items())
mydict_list = mydict.values()
print(mydict_list)

mydict = {"Anil": 200, "sunil": 300, "navya": 500}
mydict["navya"] = 1000
print(mydict)

try:
    print(mydict["koti"])
except:
    print("hey catch situation arrised")

no_of_students = 4

# mydict={}
# for x in range(0,no_of_students):
#     student_name = input("enter student name:")
#     student_Marks = input("enter the marks")
#     mydict[student_name]=student_Marks
#
# for k,v in mydict.items():
#     print(k,'===',v)

mydict = {"Anil": 200, "sunil": 300, "navya": 500}
del mydict["Anil"]
print(mydict)
mydict["Ak"] = 900
print(mydict)

print(len(mydict))
print(mydict['navya'])
mydict.pop('sunil')
print(mydict)

mydict = {"Anil": 200, "sunil": 300, "navya": 500}
for x in mydict.keys():
    print(x)

vowels = ['a', 'e', 'i', 'o', 'u']
word = "anil"
mydict = {}
for x in word:

    if x in vowels:
        if x in mydict:
            mydict[x] = mydict[x] + 1
        else:
            mydict[x] = 1

for k, v in mydict.items():
    print(k, "--", v)

squares = [x * x for x in range(0, 10) if x % 2 == 0]
print(squares)
map_squares = {x: x * x for x in range(0, 10)}
print(map_squares)

mydict = {
    "car": ['volks', 'benz', 'bmw'],
    "tyres": [10, 20, 30],
    "shades": ['black', 'chrome', 'silver'],
    "color": ['orange'],
    "price": ["200k"]
}

print(mydict['car'][1])

for k, v in mydict.items():
    for x in v:
        print(k, "====", x)

mydict = {
    "alpha": [22, 4, 5, 66, 9],
    "beta": [833, 9, 1, 3]
}

for k, v in mydict.items():
    mydict[k] = sorted(v)
for k,v in mydict.items():
    print(k ,"===",v)
