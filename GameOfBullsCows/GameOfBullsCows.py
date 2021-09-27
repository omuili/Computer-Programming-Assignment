# Import required module
import random

print("""Welcome to the game of BULLS and COWS.
The objective in this game is for you to guess a 4-digit number
The computer responds with how close your guess is to the target
BULLS = # common digits with exact matches and
COWS  = # common digits in wrong position.""")

# Returns list of digits 
# of a number
def extract_digits(num):
    snum = str(num)
    return [int(snum[0]), int(snum[1]), int(snum[2]), int(snum[3])]

    # Returns True if number has 
# no duplicate digits 
# otherwise False 
def no_repeating_digits(num):
    digits = extract_digits(num)
    if digits[0] != digits[1] and \
       digits[0] != digits[2] and \
       digits[0] != digits[3] and \
       digits[1] != digits[2] and \
       digits[1] != digits[3] and \
       digits[2] != digits[3]:
        return True
    else:
        return False 

    # Generates a 4 digit number 
# with no repeated digits 
def produce_target():
    while True:
        num = random.randint(1000,9999)
        if no_repeating_digits(num):
            break
    return num

   # Returns common digits with exact 
# matches (bulls) and the common 
# digits in wrong position (cows)
def numOfBullsCows(num,guess):
    bull_cow = [0,0]
    num_li = extract_digits(num)
    guess_li = extract_digits(guess)
      
    for i,j in zip(num_li,guess_li):
          
        # common digit present
        if j in num_li:
          
            # common digit exact match
            if j == i:
                bull_cow[0] += 1
              
            # common digit match but in wrong position
            else:
                bull_cow[1] += 1
                  
    return bull_cow

# Secret Code
num = produce_target()
tries =int(input('Enter number of tries: '))

# Play game until correct guess 
# or till no tries left
while tries > 0:
    guess = int(input("Enter guess number: "))

    if not no_repeating_digits(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
      
    bull_cow = numOfBullsCows(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -=1
      
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")