num = 0

while True:
    try :
        a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        if a not in [1,2,3]:
            print("1, 2, 3 중 하나를 입력하세요.")
        else:
            break
    except ValueError:
        print ("정수를 입력하세요.")