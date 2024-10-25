import csv


class filehandling:

    def Method_1(self):
        print('hey printing the file ')
        f = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/abc.txt", "w+")
        print(f'printing file name {f.name}')
        print(f'printing the file Mode {f.mode}')
        print(f'printing the file is readable {f.readable()}')
        print(f'printing the file is writable {f.writable()}')
        print(f'printing the file is closed {f.closed}')
        f.close()
        print(f'printing the file is closed {f.closed}')
        print('calling method m1 from m2')

    def Method_M2(self):

        try:
            print('hey printing the second file ')
            f2 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/abc.txt", "w+")
            f2.write('hey this is second line ')
            f2.close()
            f3 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/abc.txt", "w+")
            f3.write('hey this  as third Line \n')
            f3.write('hey this is  as fourth Line')
            f3.close()
            f4 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/abc.txt", "a+")
            f4.write('\nappended last line ')
            f4.seek(0)
            data = f4.read()
            print(f'data is : {data}')


        except(Exception) as msg:

            print(f'hey the except is going good {msg}')

        finally:
            print('Hey this is cleaning code ')

    def method_m3(self):
        print('Printing the Method M3')
        str = "hey dude hellow how are you !"
        mylist = str.split(" ")
        print(mylist)
        fm3 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/abc.txt", "a+")
        fm3.writelines(mylist)
        fm3.seek(0)
        data = fm3.read()
        print(data)
        print(f'printing the reading : {data}')

    def method_M4(self):

        try:
            fm3 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/xyz.txt", "r")
            data = fm3.read()
            fm3.seek(0)
            print(f'data is {data}')
            print('=============')
            print(fm3.readline())
            Lines = fm3.readlines()
            for line in Lines:
                print(line)

        except (Exception) as msg:
            print(f'Landing into Except catch block {msg}')

        finally:
            print('cleaning up the code ')

    def method_m5(self, mydict):
        try:
            flag = False
            for key, val in mydict.items():
                for each_key, each_val in val.items():
                    print(f'outer key is {key} inner key is   {each_key} inner val is {each_val}')
                    if each_val == 'ORC':
                        return True
            return flag


        except Exception as msg:
            print(f'we are in catch block of M5 method and {msg}')
            return flag

    def method_m6(self):

        with open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/xyz.txt", "r") as f:
            print(f.seek(0))
            lcount = ccount = wcount = 0
            for line in f:
                lcount = lcount + 1
                ccount = ccount + len(line)
                words = line.split()
                wcount = wcount + len(words)

            print(f'l_count : {lcount} and c_count :{ccount} and w_count :{wcount}')

    def method_m7(self):

        try:

            f1 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/xyz.txt", "rb")
            f2 = open("/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/xyz_B.txt", "wb")
            # data = f1.read()
            f2.write(f1.read())
        except Exception as msg:
            print(f'{msg}')

    def method_m8(self):

        try:

            fb = open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/Player.csv', 'r')
            reader = csv.reader(fb)
            data = list(reader)

            for line in data:
                for word in line:
                    print(word, "\t", end='')
                print()
        except Exception as msg:
            print(f'we are in except : {msg}')
        finally:
            print("hello cleaning the code ")

    def method_m9(self):
        with open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/Team.csv', 'r') as fb:
            reader = csv.reader(fb)
            data = list(reader)

            for line in data:
                for word in line:
                    print(word, '\t', end='')
                print()

    def method_m10(self):

        try:
            with open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/Team.csv', 'w', newline='') as fw:
                writer = csv.writer(fw)
                writer.writerow(["Student_name", "Student_course", "Student_Age"])
                for i in range(3):
                    print('val')
                    Student_name = input(" Enter the Student name :")
                    Student_course = input('enter the student Course :')
                    Student_Age = input('Enter the student Age : ')
                    writer.writerow([Student_name, Student_course, Student_Age])

            print('Total Number of Employess saved Sucesfully')


        except Exception as msg:
            print(f'Exception is :{msg}')

    def method_m11(self):

        try:
            print()
            with open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/Team_new.csv', 'w', newline='') as fw:
                writer = csv.writer(fw)
                writer.writerow(['Employee_No', 'Employee_Name', 'Employee_sal'])
                for i in range(2):
                    Employee_No = input('enter Employee NO :')
                    Employee_Name = input('Enter the Employee Name :')
                    Employee_Sal = input('Enter the Employee salary :')
                    writer.writerow([Employee_No, Employee_Name, Employee_Sal])

            with open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/Team_new.csv', 'r') as fr:
                reader = csv.reader(fr)
                data = list(reader)
                for line in data:
                    for word in line:
                        print(word, '\t', end='')
                    print()

        except Exception as msg:
            print(f' Exception : {msg}')
        finally:
            print(f'code save sucesfully')

    def Method_m12(self):
        try:
            print()
            with open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/slippers.csv', 'w', newline='') as fw:
                writer = csv.writer(fw)
                writer.writerow(['Feet_size', 'Feet_style', 'price'])
                for i in range(2):
                    Feet_size = input('please give feet size')
                    Feet_style = input('please give the feet style')
                    price = input('please give the feet price')
                    writer.writerow([Feet_size, Feet_style, price])

            with open('/Users/navyasree/Desktop/ANIL_JOB_DOCS_MAIN/slippers.csv', 'r') as fr:
                reader = csv.reader(fr)
                data = list(reader)
                for line in data:
                    for word in line:
                     print(word, '\t', end='')
                    print( )


        except Exception as msg:
            print(f'{msg}')
        finally:
            print()


obj1 = filehandling()
obj1.Method_m12()

mydict = {'anil': ['vw', 'swift', 'Benz'],
          'hanok': ['Benz', 'cruiser']}

mydict_1 = {'anil': {'employee': 'epam', 'salary': 3000, 'city': 'AD'},
            'navya': {'employee': 'ORC', 'salary': 4000, 'city': 'DB', 'channel': 'capital'}
            }

# val=obj1.method_m5(mydict_1)
# print(f'method_m5 returned value is {val}')
