#!!NUMBER GUESSING GAME!!!
#CREATED BY GANGA SINGH


import random

while(1):
        
                        again=input("DO YOU WANT TO PLAY(enter y/n):")
                        if again=="y" or again=="Y":
                                print("\t\t!!WELCOME TO THE NUMBER GUESSING GAME!! :)")
                                print("\t\tLETS GET STARTED")
                                lower = int(input("enter lower bound:"))
                                upper = int(input("enter upper bound:"))
                                if upper<100:
                                        print("MODE:EASY")
                                elif upper>100 and upper<500:
                                        print("MODE:MODERATE")
                                elif upper>500:
                                        print("MODE:HARD")
                        
                                x = random.randint(lower, upper)
                                print("\n\tYou have got 10 chances to guess the NUMBER!!!!\n")

                                count = 0
                                while count < 10:
                                        count=count+1

                                        guess = int(input("GUESS A NUMBER!!:"))
                                        if x == guess:
                                                print("WOW!! OP!! You have guessed the number in ",
                                                      count, "try")
                                                break
                                        elif x > guess:
                                                print("Your guessed number is smaller than the origianl number!!!")
                                        elif x < guess:
                                                print("Your guessed number is greater than the origianl number!!!")

                                        if count >= 10:
                                                print("\n\t!!!GAME OVER!!!you have exceeded your chances :'(")
                                                print("\n The Number is ",x," O_O")


                               

                               
                        elif again=="n" or again=="N":
                                print("\nTHANK YOU!! SEE YOU AGAIN!!")
                                break
        
