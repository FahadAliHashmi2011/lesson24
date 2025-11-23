class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter String : ")

    def print_String(self):
        print("Result is :", self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
#==========================-------------------------------------=============================
class Employee:
    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
