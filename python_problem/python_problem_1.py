import sys

num = 0

def inputNum():
    while True:
        try :
            a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if a not in [1,2,3]:
                print("1, 2, 3 중 하나를 입력하세요.")
            else:
                return a
        except ValueError:
            print ("정수를 입력하세요.")

status = 0

while (True):
    if status == 0:
        count = inputNum()
        for i in range(count):
            num = num+1
            print ("Player A :", num)
            if (num == 31):
                print ("Player B Win!")
                sys.exit()
        status = 1

    else :
        count = inputNum()
        for i in range(count):
            num = num+1
            print ("Player B :", num)
            if (num == 31):
                print ("Player A Win!")
                sys.exit()
        status = 0

