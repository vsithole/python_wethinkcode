import random

def run_game():
 
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    turns = 12
    oriDigi=[]
    for i in range (4):
        newInt = random.randint(1,8)
        while newInt in oriDigi:
            newInt = random.randint(1,8)  
        oriDigi.append(newInt)
        
    while turns != 0:
        try:
            digits = input("Input 4 digit code: ")
            if len(digits) == 4 and digits.isdigit(): 
                lstdigits = list(digits)
                oriDigi_ = list(oriDigi)
                
                d = list(map(str,oriDigi_))
                v = ''.join(map(str,d))
            
                countPos = 0
                countAvail = 0
                for z in range(len(d)):
                    if d[z] == lstdigits[z]:
                        countPos+=1
                    elif lstdigits[z] in d:
                        countAvail+=1
                
                if countPos == 4:
                    print("Number of correct digits in correct place:     "+ str(countPos))
                    print("Number of correct digits not in correct place: "+ str(countAvail))
                    print("Congratulations! You are a codebreaker!")
                    print("The code was: "+v)
                    break
                else:
                    turns-=1
                    print("Number of correct digits in correct place:     "+ str(countPos))
                    print("Number of correct digits not in correct place: "+ str(countAvail))
                    print("Turns left: "+str(turns)) 
            else:
                print("Please enter exactly 4 digits.")
                continue
        except (EOFError):
            print(end="")
            break  

if __name__ == "__main__":
    run_game()
