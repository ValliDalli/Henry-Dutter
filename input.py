import wordle
filename='words.txt'
with open(filename) as text:
    content=text.read()
words=content.split()
print("this is a Program that solves Wordle, you are first asked wich guess you entered in wordle an after that you should enter the result you got after entering your guess in wordle")
print("You enter the result like that for example: ywgyy this means your first letter was yellow the second white third green")
print("g: green, y: yello,w: white")
print("after that the Program presents you all the possible words for your next guess and you can repeat everything till you find the correct word")
print("if you want to quit because you found the solution you can write quit when you are asked for a guest")
while(True):
    guess=input("what was your guess? ")
    if(guess=="quit"):
        print("nice job:-)")
        break
    result=input("enter the result one word? ")
    position=0
    for x,y in zip(guess,result):
        
        substring=guess[0:position]
        #print(f"substring: {substring}, po")

        if(y=='w') and (x in substring ):#check edge case
            count_x=substring.count(x)# it shows how often the letter is allowed to appeared in the solution word
            x_position=substring.find(x)
            y_position=result[0:position].find('y')
            g_position=result[0:position].find('g')
            if(y_position<g_position):
                y_position=g_position 
            print("hmm")
            if(x_position==y_position):
                words=wordle.edge_case(position,x,words,count_x)
                print("einschlag0")

        elif(y=='g'): #Letter was green
            words=wordle.green(position,x,words)
            print("einschlag1")
            
        elif(y=='y'): #letter was yellow
            words=wordle.yellow(position,x,words)
            print("einschlag2")
            
        elif(y=='w'): #letter was white
            words=wordle.white(x,words)
            print("einschlag3")
        position+=1
        
        
            
        
    print(words)
