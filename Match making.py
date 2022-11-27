def match_making(name1, name2):
        vowels = "AaEeIiOoUu"
        count=0
        count2 = 0
        for i in name1:
                if i in vowels:
                    count+=5
                else:
                    count-=1
                
        for j in name2:
            if j in vowels:
                count2+=5
            else:
                count2-=1
        if abs(count-count2) <=5:
            print("you're soulmates")
        elif abs(count- count2) >6 and abs(count - count2)<10:
            print("decent match")
        else:
            print("may try elsewhere")



