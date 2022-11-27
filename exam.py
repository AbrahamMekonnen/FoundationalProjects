'''
def no42(lyst):
    for i in lyst:
        if 42 in lyst:
            return True
        return False
no42([42, -4, 17])       

def lowecase(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
lowecase("aaHHDhds")

my_student = {}
my_friend = {'John': 5}
my_student('John') = 5
print(my_student)
'''

mulitiple = 1
with open("num.txt", "r+") as f:
    read = f.readlines()
    for i in range(len(read)):
        if read[i].isdigit():
               mulitiple *= read[i]
    print(mulitiple)

