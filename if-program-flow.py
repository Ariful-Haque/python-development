#!/usr/local/bin/python3.7

#name = input("Please enter your name: ")
#age = int(input("How old are you, {0}? ".format(name)))
#print(age)
#
#if age >= 18:
#    print("You are old enough to vote.")
#    print("Please put an X in the ballot box.")
#else:
#    print("Please come back in {0} years.".format(18 - age))
#

#----------------------------------
# to comment out a block of code
  # visualize it at first
  # :   norm i#
  # and to uncomment, norm x

# ----------------------------------

print("Please guess a number between 1 and 10: ")
guess = int(input())

#if guess < 5:
#    print("Please guess higher: ")
#    guess = int(input())
#    if guess == 5:
#        print("You guessed it!")
#    else:
#        print("You have not guessed correctly.")
#elif guess > 5:
#    print("Please guess lower: ")
#    guess = int(input())
#    if guess == 5:
#        print("You have guessed it!")
#    else:
#        print("You have not guessed correctly.")
#else:
#    print("You guessed it first time!")
#

# ----------------------------------------
# the above code can be written more efficiently

if guess != 5:
    if guess < 5:
        print("Please guess higher: ")
    else:
        print("Please guess lower: ")
    guess = int(input())
    if guess == 5:
        print("You have guessed it.")
    else:
        print("You have not guessed correctly.")
else:
    print("You got it first time!!")













