#Abraham, this code does bunch of things using a file as an input.
#date - 10/15/2022
#Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
#Info on ports here: https://support.desk.com/customer/portal/articles/1741-configuring-smtp-servers-to-send-email

import uuid #forgot where I learned this from
import re
import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
read1 = []                    
numbers = []

def hundred_characters():#prints 100 characters
    word_count = input("enter a word to print: ")
    for i in range(len(read1)):
        if read1[i] in word_count:#checks if the word is in the list, then prints 50 characters before and after.
            print(*read1[i-50:i+50])
            break
def replace_word():#replaces a word and prints it if neccessary
    search =input("enter a word to replace: ")
    replaced = input("enter a word to replace it by: ")
    l = list(map(lambda x : x.replace(search, replaced),read1))#replaces a word with another word from the read1 list
    request = input("wold you like to print the file [yes/no]? ")
    if request == "yes" or request == "Yes":
        print(l)
    else:
        quit
    
def new_file(read, shift):#shifts the text in a new file, every time a new file with a new name is created.
    global shifted
    shifted = ""
    text = read.lower()
    abc = "qwertyuiopasdfghjklzxcvbnm"
    for i in read:
        if i in abc:
            value = ord(i)+shift
            if value > 122:
                shifted += chr(value-26)
            else:
                shifted += chr(value)
        else:
            shifted+= i

    filename = str(uuid.uuid4()) + ".txt"#creates a new name for the new file
    with open(filename,"w+") as f:
        for write in read:
            written = f.write(shifted)
            break
    print("the file has been breated. Name of new  file created is "+ filename)
def remove_numbers():#first replaces numbers with a empty string then removes the string
    for i in read1:
        num = re.sub('[0-9]+',"", i)#subs numbers with empty strings
        numbers.append(num)
        if "" in numbers:
            numbers.remove("")
    print(*numbers)
sentences = ""#stores sentences from read1 as a string
def phrase():
    global sentences
    for i in range(len(read1)):
        if read[i] in ".":
            sentences = sentences + " ".join(read1[i+1:i+50])#stores the words after a priod in sentences
            return sentences
def sendEmail(sender, sendee, header, body, password):#to send email
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(sender, password)
    msg = MIMEMultipart()
    msg['From']= sender
    msg['To']= sendee
    msg['Subject']= header
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()


content = ""
def table_contents():
    try:
        global content
        while content != "7":
            print("1.count \n" + "2. print 100 characters of the specific word\n" + "3. replace a word \n" + "4. Create a new file\n" + "5. remove numbers\n" + "6. send email\n" + "7. quit")
            content = input("pick one number from the lists of contents: ")
            if content== "1":#couts the word provided by the user
                count_word = input("enter a word or phrase: ")
                amount = read1.count(count_word)
                print(amount, "letters")
            if content =="2":#calls hudredcharachters function
                hundred_characters()
            if content =="3":#calls reaplace_word function
                replace_word()
            if content == "4":#gets number of shifts and calls the new file function
                shift = int(input("how many letters do you want the file to be shifted by? "))
                new_file(read, shift)
            if content == "5":#calls remove numebers function
                remove_numbers()
            if content =="6":#calls phrase function
                phrase()
                email = input("Enter your email: ")
                sendEmail("pythonatemu@outlook.com", email, "Testing", sentences, "1qazse4r")
            if content =="7":#quits
                break
    except:
            print("only accept numbers from 1 to 7")
            table_contents()

def open_file(): #this opens the file, reads it, splits it to use it in the above functions.
    global read
    global read1
    try:
        print("enter a file:")
        file_text = input()
        with open(file_text,encoding="utf8", errors='ignore') as f:
            read = f.read()
            read2 = read.split()
            read1= read1 + read2
            table_contents()
    except:
        print("File doesn't exist, try again. ")
        open_file()
open_file()

