import sys
import random

num = 0
status = 0
def brGame():
    while True:
        try :
            a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if a not in [1,2,3]:
                print("1, 2, 3 중 하나를 입력하세요.")
            else:
                return a
        except ValueError:
            print ("정수를 입력하세요.")


while (True):
    if status == 0:
        count = random.randint(1,3)
        for i in range(count):
            num = num+1
            print ("Computer :", num)
            if (num == 31):
                print ("Player Win!")
                sys.exit()
        status = 1

    else :
        count = brGame()
        for i in range(count):
            num = num+1
            print ("Player :", num)
            if (num == 31):
                print ("Computer Win!")
                sys.exit()
        status = 0
