import random

# TODO: Decompose into functions

def get_a_guess():
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')   

    return code


def get_user_code():
    answer = input("Input 4 digit code: ")
    return answer
    

def check_result(code, answer):
        
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    return correct_digits_and_position


def show_result(correct, correct_digits_and_position, turns):
    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))                         
    return correct


def run_game():
    code = get_a_guess()
        
    correct = False
    turns = 0
    while not correct and turns < 12:
      
        answer = get_user_code()
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        else: 
            correct_digits_and_position = check_result(code,answer)
            turns += 1 
            correct = show_result(correct, correct_digits_and_position, turns)
            if correct == True:
                break

    print('The code was: '+str(code))

if __name__ == "__main__":
    run_game()
