#packages imported
import random
import os
import math

#all variables used
option = ()
  #option 1 variables
triangle_base = 0
triangle_height = 0
triangle_total = 0
  #option 2 variables
square_variable = 0
square_total = 0
  #option 3 variables
hexagon_side = 0
hexagon_total = 0
  #option 4 variables
perimeter_side = 0
perimeter_count = 0
perimeter_total = 0
  #option 5 variables
dice_used = 0
dice_rolled = 0
number_rolled = 0
user_score = 0
computer_score = 0
game_chances = 0
reroll = ''
c_reroll = 0
DIF = 0
  #option 6 variables
words = ["umbrella", "pizza", "pickles", "water", "president", "liability", "apples", "faces", "children", "bunny", "squids", "magical", "bright", "mountain", "lockets", "abstract", "singing", "plague", "creator", "rain", "moon", "quitter", "football", 'tennis', 'imagination', 'electronic']
word_choice = random.choice(words)
guess = ''
user_word = ''
finish = 0
correct = 0
guess_wrong = ''
guess_input = ''
  #options 7 variables
day = 0
dead = 1
zombie = random.randint(2,999)
weapon_p = 1
ammo = random.randint(500,1000)
while ammo < zombie :
  ammo = random.randint(500,1000)
cash = 0
game_option = 0
total_p = 0
price = 500
buy = 0
no_new_day = 1
location = 0
lock_location = False
ammo_s = 0
ammo_buy = 0
high_score = 0
increasing_zombie = 0
increasing_cash = 0
invest = 0
invest_amount = 0
invest_time = 0
invest_made = 0
invest_first = 0
invest_second = 0
game_started = 0
  #option 8 variables
slot_roll = 0
slot_1 = 0
slot_2 = 0
slot_3 = 0
slot_cash = 1000
losing_prompt = ["aw shucks, you lost.", "that too bad, you lost", "your pretty bad at this game, as you just lost", "try again.", "did you know that a starfish can release up to 2.5 million eggs? no? well, did you know that you lost? probably.", "Im running ways to tell you that you lost", "thou has' undeniably forfeited thee match.", ]
prompt_randomizer = random.randint(0,6)
slot_cash_debt = 30
prompt_stopper = 0
  #option 9 variables
distance = 0
speed = 0


print("This is my weird math thingy. Enjoy!")

#loops the program

while 7 != 1 :

  #prompt

  print("\nwhich would you like to do?")

  #prints the options and takes in the option choice
  print("mathy area:")
  print("1: Area of an equilateral triangle")
  print("2: Area of a square")
  print("3: Area of a hexagon")
  print("4: Perimeter of any equal shape")
  print("games")
  print("5: Dice game")
  print("6: Hangman")
  print("7: Zombie survival")
  print("8: Slot machine")
  option = input("")
  os.system('clear')


  #runs option 1 if user inputs as such


  if option == ("1"):

    #sets the triangles values to 0 for the math.

    triangle_base = 0
    triangle_height = 0
    triangle_total = 0

    #takes in the user inputed variables

    triangle_base = float(input("The equation for finding an equilateral triangle is 1/2*B*H. What is the Base?\n"))
    triangle_height = float(input("What is the height?\n"))

    #the math of the total triangle.

    triangle_total = (float(triangle_height) * float(triangle_base))/2

    #prints the total area.

    print("the area of the triangle is " + str(triangle_total))


  #runs option 2 if user inputs as such


  if option == ("2") :
    
    #resets the square values for the math
    square_variable = 0
    square_total = 0

    # takes in the usre inputed variables

    square_variable = input("The equation for finding the area of a square is base or height squared. What is the base or the height?\n")

    #the math of the total square

    square_total = float(square_variable) ** 2

    #prints out the total area

    print("The area of the sqaure is " + str(square_total))


  #runs option 3 if the user inputs as such


  if option == ("3") :
    
    #resets the values for the math
    
    hexagon_side = 0
    hexagon_total = 0

    #takes in the needed variable(s) for the math

    hexagon_side = float(input("The area of a hexagon is (3√3 * A Side * 2) / 2. what is the given side?\n"))

    #the math that finds the total. (I totally copied this part from a website. I couldnt figure out how to do the square root.)

    hexagon_total = area=(3*math.sqrt(3)*math.pow(hexagon_side,2))/2.0

    #prints the total

    print("the total area of the hexagon is " + str(hexagon_total))


  #runs option 4 if the user inputs as such


  if option == ("4") :

    #resets the values for the math

    perimeter_side = 0
    perimeter_count = 0
    perimeter_total = 0
    
    #takes in the required variables for the math

    perimeter_side = float(input("The permimeter any equal shape is found by multiplying the side length and the amount of sides. What is the side length?\n"))
    perimeter_count = int(input("How many sides are there?\n"))

    #The math to find the total perimeter

    perimeter_total = perimeter_side * perimeter_count

    #prints the total

    print("the perimeter of this shape is " + str(perimeter_total))


  #runs option 5 if the user inputs as such


  if option == ("5") :

    #resets all variables used for each game

    dice_used = 0
    dice_rolled = 0
    number_rolled = 0
    user_score = 0
    computer_score = 0
    game_chances = 0
    reroll = ''
    c_reroll = 0
    DIF = 0

    #opening prompt and takes in the amount of dice to be rolled for each player

    dice_used = int(input("This game is like bad yhatzee. You will roll 2-6 dice up to 3 times. The computer will do the same and try to beat your score. How many dice do you want to roll?\n"))

    #if the user imputed too high of a value, it will be set to six
    if dice_used > 6 :
      dice_used = 6

    #the gambiling part of the game

    while game_chances < 3 :
      while dice_rolled < dice_used :
        number_rolled = random.randint(1,6)
        user_score += number_rolled
        print("You have rolled a " + str(number_rolled) + ". You have " + str(user_score) +"points.")
        dice_rolled += 1

        # if you havent rerolled 3 times already, you are given the option to reroll.
      if game_chances != 3:
        reroll = str(input("Would you like to reroll your dice? (Y) (N)\n"))
        if reroll == 'Y' :
          user_score = 0
          dice_rolled = 0
          game_chances += 1
        else :
          dice_rolled = 0
          game_chances = 5
    print("Computers turn:")
    dice_rolled = 0

    # the computers turn to roll the dice

    while c_reroll < 3 :
      while dice_rolled < dice_used :
        number_rolled = random.randint(1,6)
        computer_score += number_rolled
        print("The computer has rolled a " + str(number_rolled) + ". They now have " + str(computer_score) + " points.")
        dice_rolled += 1

      # if the computer lost, it will automatically reroll until either it has rerolled 3 times or it Wins

      if computer_score < user_score :
        c_reroll += 1
        dice_rolled = 0
        computer_score = 0
        print("Computer has chosen to reroll.")
      else:
        c_reroll = 5

    #prints out the winner and the difference between their scores

    if computer_score > user_score :
      DIF = computer_score - user_score
      print("you have lost by " + str(DIF) + " points.")
    elif computer_score < user_score :
      DIF = user_score - computer_score
      print("you have won by " + str(DIF) + " points! good job!")
    else :
      print("you managed to tie a robot. congrats...?")


  #runs option 6 if the user inputs as such

    # for this one, while I did the coding myself, I took the concepts from my brothers project, which he did something similar.

  if option == ("6") :
    print("this is my badly made hangman game. you have 10 lives to guess the word. ""="" Means vowels ")
    
    #reseting all the variables
    finish_fixer = 0
    finish = 0
    word_choice = random.choice(words)
    guess = ''
    user_word = ''
    finish = 0
    correct = 0
    guess_wrong = ''
    guess_input = ''

    while finish < 12:
      finish_fixer = 0
      if finish == 10:
        print("What is your LAST guess?")

      else:
        print("what is your guess? (single letters only!)")
      print("you have guessed guessed the following letters already: " + str(guess))
      user_word = ''
      guess_input = input('')
      guess_wrong = 1

      while guess_wrong == 1:

        if guess_input in guess:
          print("Please enter only one word")
          guess_input = input('')

        elif len(guess_input) != 1:
          print("Please enter only one letter")
          guess_input = input('')

        elif guess_input == int:
          print("Please enter a letter")

        else:
          guess_wrong = 0
          guess += guess_input
      os.system('clear')

      
      for i in word_choice:
        correct = 0

        for j in guess:

          if j == i:
            user_word += j
            correct = 1

        if correct == 0:
          if finish_fixer == 0:
            finish += 1
            finish_fixer = 1
          if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            user_word += '='
          else:
            user_word += '_'
          correct = 0

      print(user_word)
      if user_word == word_choice:
        finish = 100
        print("you win. congragulations!")
      elif finish == 11:
        finish = 100
        print("too bad, you lose. The word was " + str(word_choice))

  #runs option 7 if the user inputs as such

  if option == ("7"):
    print("allowed inputs: 1(yes), 2(no)")
    play = int(input("This is my zombie survival game that I made before, then copied onto here. Would you like to play?\n"))

      #variables reset after every new day

    while play == 1 :
      if no_new_day == 1 :
        dead = 0
        game_option = 0
        total_p = 0
        day += 1
        location = 0
        increasing_cash = 0 + (day * 15)
        cash += ((200 + increasing_cash))
        increasing_zombie = 0 + (day * 40) 
        zombie = random.randint((2 + increasing_zombie) ,(950 + increasing_zombie))

        #reseting all the games attributes after every new game

        if game_started == 0 :
          day = 1
          increasing_zombie = 0
          increasing_cash = 0
          no_new_day = 1
          location = 0
          lock_location = False
          ammo_s = 0
          ammo_buy = 0
          price = 500
          buy = 0
          weapon_p = 1
          invest_first = 0
          invest_second = 0
          invest = 0
          invest_amount = 0
          invest_time = 0
          invest_made = 0
          cash = random.randint(250,499)
          ammo = random.randint(500,1000)
          zombie = random.randint(2,999)
          while ammo < zombie :
            ammo = random.randint(500,1000)
          #the main prompt
      game_started = 1
      print("\nday " + str(day) + ": today, there are " + str(zombie) + " zombies.")
      print("you have $" + str(cash) + " to spend.")
      print("you have " + str(ammo) + " bullets to use today")
      print("your current weapon can take out " + str(weapon_p) + " zombie(s) per bullet.")
      print("what would you like to do?")
      print("1: fight the zombies (ends the day)")
      print("2: shop for a new weapon")
      print("3: travel to a new location")
      print("4: shop for ammo")
      print("5: invest some money")
      no_new_day = 0
      game_option = int(input())

    #if the player chose option 1

      if game_option == 1 :
        no_new_day = 1
        total_p = int(ammo) * int(weapon_p)
        if total_p <= zombie :
          dead = 1
          os.system('clear')
          print("you were unable to kill all the zombies. you have died.")
        else:
          ammo = round((int(total_p) - int(zombie))/ int(weapon_p),0)
          os.system('clear')
          print("you successfully took out the zombies with " + str(ammo) + " bullets left")
          if invest_time > 0 :
            invest_time -= 1

    #if the player chose option 2

      if game_option == 2 :
        if weapon_p == 5 :
          os.system('clear')
          print("You have reached the max power for your weapon.")
        if weapon_p < 5 :
          print("welcome to the shop!")
          print("would you like to upgrade your weapon for $" + str(price) + "?")
          buy = int(input())
          if buy == 1 :
            if cash <= price :
              os.system('clear')
              print("you do not have enough for this upgrade!")
              no_new_day = 0
            if cash >= price :
              cash = int(cash) - int(price)
              weapon_p = int(weapon_p) + 1
              price = int(price) + 500
              os.system('clear')
              print("you have bought the upgrade! you now have $" + str(cash) + ".")
              no_new_day = 0
          else :
            no_new_day = 0

    #if the player chose option 3
      
      if game_option == 3 :
        no_new_day = 0
        if lock_location == True :
          os.system('clear')
          print("you have already moved locations.")
        else :
          print("would you like to move to a new place? you may only do this once.")
          location = int(input())
          if location == 1 :
            zombie = random.randint(2,500)
            lock_location = True
            os.system('clear')
            print("you have changed locations!")
          
    #if the player chose option 4

      if game_option == 4 :
        no_new_day = 0
        print("Welcome to the ammo shop! Would you like to purchase some ammo? (1$ per bullet)")
        ammo_s = int(input())
        if ammo_s == 1 :
          ammo_buy = 0
          print("How many bullets would you like to buy?")
          ammo_buy = int(input())
          if ammo_buy > cash :
            os.system('clear')
            print("You cannot afford this ammount")
          if ammo_buy <= cash :
            ammo += ammo_buy
            cash -= ammo_buy 
            os.system('clear')
            print("You now have " + str(ammo) + " bullets and $" + str(cash) + ".")

    #if the player chose option 5
      
      if game_option == 5 :
        if invest_first == 1 :
          if invest_time == 0 :
            cash += invest_made
            invest_made = 0
            invest_second = 1
            os.system('clear')
            print("You have taken out your money! your current balance is now $" + str(cash))
          else :
            os.system('clear')
            print("the bank is not open yet. You have to wait another " + str(invest_time) + " day(s)")
        if invest_first == 0 :
          print("\nWelcome to the bank. if you put your money in, you can multiply it up to 5 times the amount. however, the bank is inconsistant. It may take a while before you can get your money back")
          print("Would you like to invest?")
          invest = int(input())
          if invest == 1 :
            print("How much would you like to invest?")
            invest_amount = int(input())
            if invest_amount > cash :
              os.system('clear')
              print("You cannot afford this investment")
            if invest_amount <= cash :
              invest_made = invest_amount * round(random.uniform(2.0, 5.0), 1)
              invest_made = round(float(invest_made),0)
              invest_time = random.randint(2,5)
              cash = int(cash) - int(invest_amount)
              invest_first = 1
              os.system('clear')
              print("You have invested $" + str(invest_amount) + ". come back in " + str(invest_time) + " days to get your money back.")
        if invest_second == 1 :
          invest_first = 0
          invest_second = 0

    #if the player died        
      
      if dead == 1 :
        if high_score < day :
          high_score = day
        print("You lasted for " + str(day) + " day(s). Would you like to play again?")
        day = 0
        no_new_day = 1
        invest_made = 0
        play = int(input())
        if play != 1 :
          os.system('clear')
          game_started +=1
          print("your highest day was " + str(high_score) + ". Congrats!")
        if play == 1 :
          game_started = 0      

  #runs option 8 if the user inputs as such

  if option == ("8"):

    # the main prompt. takes in if the user would like the gamble or not.
    print("Welcome to the casino! Would you like to roll the machine for $100? you currently have $" + str(slot_cash) + ". (y) (n)")
    slot_roll = input("")

    #cheks if the user wants to play the game (again)

    if slot_roll == ("y") or slot_roll == ("Y"):
      slot_roll.lower()
      while slot_roll == ("y"):
        os.system('clear')

        #takes away money and rolls 3 dice

        slot_cash -= 100
        slot_1 = random.randint(1,35)
        slot_2 = random.randint(1,35)
        slot_3 = random.randint(1,35)
        print("You rolled a " + str(slot_1) + ".")
        print("You rolled a " + str(slot_2) + ".")
        print("you rolled a " + str(slot_3) + ".")

        #cheks if the user won or not and prints and adds money off of that

        if slot_1 == slot_2 or slot_2 == slot_3 or slot_1 == slot_3:
          if slot_1 == slot_2 and slot_2 == slot_3:
            print("JACKPOT!!! You won $100,000!!!")
            slot_cash += 100000
          else:
            print("Minor jackpot! you won $1,000!")
            slot_cash += 1000
        else:
          print(losing_prompt[random.randint(0,6)])
          
          #checks if the user is in debt. this prompt will only be displayed once.

        if slot_cash < 0:
          if prompt_stopper == 0:
            print("you have entered debt. you may continue to roll, but your debt will continue to grow the longer you stay in debt.")
            prompt_stopper = 1
          slot_cash_debt *= 1.1
          slot_cash -= slot_cash_debt

          #checks if the user wants to play again

        print("you now have $" + str(slot_cash) + ". would you like to roll again? (y) (n)")
        slot_roll = input()  