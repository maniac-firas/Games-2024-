import random, time
from movement import printrows, right, left, up, down, err
from functions import check

matr = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

r = random.randint(0,3)
c = random.randint(0, 3)
matr[r][c] = 2
error = False

def play():
     global game, error, r, c, matr, larg
     init = time.time()
     while game == "True":
          pro = True
          while pro and not(error):
               r = random.randint(0,3)
               c = random.randint(0, 3)
               if matr[r][c] == 0:
                    matr[r][c] = 2
                    pro = False
               else: pro = True

          if error: error = False

          print(r+1,"X", c+1)
          printrows(matr)
          game, max = check(matr)
          opt = input("Enter key:")
          print('\n'*5)

          if opt == '8':   up(matr)
          elif opt == '6': right(matr)
          elif opt == '2': down(matr)
          elif opt == '4': left(matr)
          elif opt == 'e' or opt == 'E': break
          else: error = err()
     final = time.time()

     if game == "OVER":
          total = final - init
          name = input("\nEnter name:")
          with open("Highscore.txt", "a+") as hs:
               cond = True
               for row in hs.readlines():
                    if row[0] == name:
                         row[1] = total
                         row[2] = max
                         cond = False
               if cond:  hs.write(nametotal, max)
               

while True:
     print("2048 Game in Python. Made in 2024.")
     print("1. Play")
     print("2. Highscore")
     print("0. Exit")

     op = int(input("Enter Option to choose:"))
     if op == 1:
          game = "True"
          play()

     elif op == 2:
          with open("Highscore.txt", "r") as hs:
               for row in hs.readlines():
                    print("\n", row[0], ":", row[1], ":", row[2])

     elif op == 0:
          exit()
          break

     else:
          print("Option not correct.")



     
