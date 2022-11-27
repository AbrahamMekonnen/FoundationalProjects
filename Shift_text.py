#Abraham
#names of students in class, Monty Python: The Argument Sketch, Time and the Rani, Gadsby, Team members of Minor League Baseball
def caesar(text, shift):
    global shifted
    shifted = ""
    text = text.lower()
    abc = "qwertyuiopasdfghjklzxcvbnm"
    for i in text:
        if i in abc:
            value = ord(i)+shift
            if value > 122:
                shifted += chr(value-26)
            else:
                shifted += chr(value)
        else:
            shifted+= i

    print(shifted)
def checker(text,shift):
    caesar(text, shift)
    print("does the sample printed make sense[y/n]? ")
    user_d = input()
    if user_d == 'y':
        return True
    return False
def decode():
    try:
        print("enter a text file: ")
        file = input()
        with open(file) as f:
            input_file = f.read()
        for i in range(40):
            count= i
            if checker(input_file, 1+i) == True:
                break
        print(count, "shifts")  
    except:
        print("only accept files")
        decode()
#input_file.split()
#for i in range(1,26):
#checker(input_file,i)
decode()
