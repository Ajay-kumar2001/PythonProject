import random
rock=''''
     _____
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''
paper=''''
   _______
---   ____)____  
          ______)  
          _______)  
         _______)
---.__________) 

  '''
scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
game_img=[rock,paper,scissors]
while True: 
    user_choise=int(input("enter the choice  \n for rock 0\nfor  paper 1 \n for scissors 2 \n for exit 3 \n"))
    print()
    if user_choise==3:
        break
    else:
        print("user_choise is")
        print(game_img[user_choise])
        computer_choise= random.randint(0,2)
        print("computer choise")
        
        print(game_img[computer_choise])
        if computer_choise==0 and user_choise==2:
            print("YOU LOST\n")
        elif user_choise==0 and computer_choise==2:
            print("YOU WIN\n") 
        elif computer_choise>user_choise:
            print("YOU LOST\n")          
        elif user_choise>computer_choise:
             print("YOU WIN\n")
        elif user_choise==computer_choise:
            print("DRAW\n")
    if user_choise==3:
        break
    

