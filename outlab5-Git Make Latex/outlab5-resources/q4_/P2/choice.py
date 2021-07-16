import random
import pickle
import string
import sys

def fill_choice():
    dic = {}
    for _ in range(100):
        strlen = random.randrange(3, 6, 1)
        numb = random.randrange(1, 5001)
        str = ''.join(random.choice(string.ascii_uppercase) for _ in range(strlen))
        dic[numb] = str
    file = open('new_int.p', 'wb')
    pickle.dump(dic, file)
    file.close()
    return


def ask_choice():
    file = open('new_int.p', 'rb')
    dic = pickle.load(file)
    lst = [int(x) for x in list(dic)]
    file.close
    inputNum = int(input("Enter Number: "))
    if inputNum < 5000 or inputNum > 7000:
        raise ValueError("Entered number must be in range 5000-7000")
    for i in lst:
        for j in lst:
            if (i + j == inputNum) and (i != j):
                print(dic[i], i, dic[j], j)
                return
    for i in lst:
        for j in lst:
            if (i + j < inputNum) and (i != j):
                print(dic[i], i, dic[j], j)
                return
    return


if __name__ == "__main__":
    try:
        sys.argv[1]
        ask_choice()
    except IndexError:
        fill_choice()
