n=2
while n>0:
    try:
        pin = int(input("Enter the pin: "))
        if(pin==4949):
            print("Lock Opened")
            exit()
        elif n==2 and pin <= 9999 and pin >= 0 :
            print("Wrong PIN! Try again")
            n = n-1
            continue
        else :
            print("Full alarm")
            exit()
        break
    except ValueError:
        print("Full alarm")
        exit()
        break

