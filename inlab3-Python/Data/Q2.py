pin=int(input("Enter the pin: "))
if(pin==4949):
	print("Lock Opened")
	exit()
print("Wrong PIN! Try again")
pin=int(input("Enter the pin: "))
if(pin==4949):
	print("Lock Opened")
else:
	print("Full alarm")