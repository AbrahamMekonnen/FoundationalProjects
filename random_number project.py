#Abraham
#09/24/2022
#the code generates a random number between 1 and a hundred. The user is required to find the randomly-picked number to win the game. 
import random
import pyfiglet
  

name = input("what's your name?") #takes the name of the user
welcome = pyfiglet.figlet_format("Welcome to the guassing game " + name + "!", font = "slant" )
print(welcome)# calls the welcome variable which goes through the module and create the inteded 'welcom" output
user_score = []

def guess_number(name:str):
    range_1 = range(1,100) 
    random_pick = random.choice(range_1)
    print(random_pick)
    global count
    count = 0

    for i in range(5):
        while True:
            try: #allows user to pick a number
                print("pick a number between one and a hundred: ")
                input_1 = int(input())
                break
            except:#lets users know it's now allowed to enter anyting besides entegers.
                print("That's not a valid option, enter integers only.")
        count += 1 #counts the number of tries
        if input_1>random_pick: #if its the number picked is too high
            print ("too high")
        
        
        elif input_1 < random_pick:#if the number picked is too low
            print ("too low")
        else: #if the user got the right number, a pyfiglet would open.
            nice = pyfiglet.figlet_format("you got it right! Nice job!", font = "standard"  )
            print(nice)
            user_score.append(count)
            print('highest score:', min(user_score), 'attempts')
            Top_scorers() #shows the 3 top scorers
            play_again() #to play again
            break
        while i<=4:
            if 4-i== 0: #if the person loses
                loser = pyfiglet.figlet_format("You've lost the game " + name + ", you better try again!!", font = "digital"  ) #prints you lost
                print(loser)
                Top_scorers() #shows the top 3 scorers
                break
            print("lets do it again, you only got", 4-i , "chances!")
            break
            
        while i>=4: #round ends
            user_score.append(count) #adds the number of attempts into the userscore list 
            print('highest score:', min(user_score), 'attempts')# compares the rounds of user and shows the highest score
            play_again()#plays the game again
            break
def play_again(): #play again function
    while True:
        try: 
            play_again = input("would you like to play more? ")
            if play_again == "yes" or play_again == "Yes" or play_again == "Y" or play_again == "y":
                guess_number(name) #runs the function if user reponds "yes".
            elif play_again == "no" or play_again == "No" or play_again == "N" or play_agian == "n":
                 Thanks = pyfiglet.figlet_format("Thanks for playing the game " +name +", you better comeback tho!", font = "slant")
                 print(Thanks)
                 break #ends the game if user responds "no"
        except:
            print(input("that's not a valid answer, please type yes or no. \n"))
        break       
            
        

      
def Top_scorers(): #stores the top scores
    y = open("Leader_board.txt","a") #adds to a file
    y.write(str(count)+" attempts- "+name+""+" \n")# adds the name and numbr of attempts into a file
    y.close
    y = open("Leader_board.txt","r")#reads the file
    readfile = y.readlines()
    sortdata = sorted(readfile)#sorts the attempts in order
    print("Here are the top scorers: \n ")
    d=0
    for i in sortdata[0:3]:
        d+=1
        print(str(d)+"\t"+str(i))#prints the top scorers
        
guess_number(name) #main function that allows the user to guess and tells it if its low or not
#also calls the play again and top scorer funcitons when a user wins or loses a game


