import random

x = input("what's your name?")
c = 0

def guess_number(x:str):
    random_pick = random.choice(range(1,100))
    print(random_pick)
    c = 0

    for i in range(9):
        print("pick a number between one and a hundred:")
        input_1 = int(input())
        c += 1
        if input_1>random_pick:
            print ("too high")
            
        elif input_1 < random_pick:
            print ("too low")
            
        else:
            print("you got it right! good job")
            return c 
            break
        print ("lets do it again, you only got", 4-i , "chances!")

#cache = {x:c, x:c}
#def score_board(x:str, c:int):
    #if x and c in cache:
        #print("seems like you've done this before and your score was: ")
        #print(cache[x])
    #else:
        #cache[x] = score_board(x)
        #cache[c]= score_board(c)
        #return cache[x] and cache[c]
        
    
#score_board(x,c)
guess_number(x)        
play_again = input("would you like to play more?")
if play_again == "yes" or play_again == "Yes":
    guess_number(x)
else:
    quit


names = [x , "It took you " + str(c) + " attempts to guess the correct number"]
print(names)

#with open("Leader_board.txt","r+") as y:
    #y.write(x)
z = open("Leader_board.txt","a+")
z.writelines(x)
z.close()

#w =  open("Leader_board.pickle","rb")
#Leader_board = pickle.load(w)
#print(Leader_board[4])
