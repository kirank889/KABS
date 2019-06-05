# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:08:53 2019

@author: Kiyon 
"""
import random

def help():
    print("User has to select a catagory from list of items. Then user has to guess the word in maximum 5 attempts else he will lose. for each correct guess user will get 10 points. for every clue 2 points will be reduced.")

class User:
    def __init__(self):
        print("Game started !!\n\n")
        self.score = 0
        
    def Category(self):
        print("Please select option in below category:\n\n1. Animals\n2. Places\n")
        category = input("Enter option : ").strip()
        return category
        
    def game(self,word):
        i = 5
        list1 = list(word)
        while (i > 0):
            inp = input().strip()
            if inp == "clue" or inp == "Clue":
                clue = random.choice(list1)
                print("word contains alphabet {}.".format(clue))
                list1.remove(clue)
                self.score -= 2
            elif inp == word:
                self.score += 10
                i -= 1
                break
            else :
                i -= 1
                print("wrong guess. you are left with {} more chances".format(i))
        return self.score
                    
                    
                
            
            

def Animal():
    List1  = ["CAT","DOG","LION","TIGER","LEOPARD","FOX"]
    return random.choice(List1)
    
def Places():
    List1  = ["CHENNAI","BANGLORE","PUNE","MUMBAI","NAGPUR","DELHI"]
    return random.choice(List1)

if __name__ == "__main__" :
    
    print("Welcome to word damsharas!! \n\n")
    print("1. Type 'Help' for more information ")
    print("2. Type 'Start' to start the game. ")
    print("3. Type 'Quit' to quit the game. ")
    
    command = "Start"
    
    while (True):
        command = input().strip()
        
        if command == "Help" :
            help()
        elif command == "start":
            user  = User()
            carryon = True
            while(carryon):
                while(True):
                    category = user.Category()
                    if category == "1" or category == "Animal" or category == "animal":
                        word = Animal()
                        break
                    elif category == "2" or category == "Places" or category == "places":
                        word = Places()
                        break
                    elif category == "Quit" :
                        break
                    else :
                        print("wrong option.")
                print("hint!! the word contains {} letters.".format(len(word)))
                print("you have 5 attempts to guess the word. please type the word below.")
                score = user.game(word)
                print("your total score is {}".format(score))
                while(True):
                    Next = input("Shall we continue : ").strip()
                    if Next == "Yes" or Next == "yes":
                        break
                    elif Next == "No" or Next == "No" :
                        carryon = False
                        break
                    else:
                        print("wrong input.")
                    
        elif command == "Quit" :
            print("Bye!!")
            break
        
        else:
            print("Invalid Command!! Please choose correct option.")
            
    
        
