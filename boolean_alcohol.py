idade=int(input("Type your age: "))
resp= idade>=18

if resp == True:
    print("You can drink alcohol")
if resp == False:
    print("You can't drink alcohol")

#Há maneiras mais práticas de se executar essa função

idade=int(input("Type your age:"))

if idade>=18:
    print("You can drink alcohol")
    if idade>=21:
        print("You are VIP")

else:
    print("You cannot drink alcohol")
