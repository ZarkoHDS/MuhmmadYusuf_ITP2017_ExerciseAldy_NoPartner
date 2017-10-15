import sys
class cat(object):
    def __init__(self,type,price,gender,age):
        self.type=type
        self.price=price
        self.gender=gender
        self.age=age
    def info_cat(self):
        print("Type:",self.type,"\nPrice:",self.price,"\nGender:",self.gender,"\nAge:",self.age)


class dog(object):
    def __init__(self,type,price,gender,age):
        self.type=type
        self.price=price
        self.gender=gender
        self.age=age
    def info_dog(self):
        print("Type:",self.type,"\nPrice:",self.price,"\nGender:",self.gender,"\nAge:",self.age)


class bird(object):
    def __init__(self,type,price,gender,age):
        self.type=type
        self.price=price
        self.gender=gender
        self.age=age
    def info_bird(self):
        print("Type:",self.type,"\nPrice:",self.price,"\nGender:",self.gender,"\nAge:",self.age)

def chcat():
    pay= 0
    print("1.Anggora","\n2.American")
    inp=input("Choice the type :")
    if inp == "1":
        x.info_cat()
        pay += 500
        buy(inp)
        return pay
    elif inp == "2":
        c.info_cat()
        pay += 600
        buy(inp)
        return pay

def chdog():
    pay= 0
    print("1.Husky","\n2.Doge")
    inp=input("Choice the type :")
    if inp == "1":
        z.info_dog()
        pay += 800
        buy(inp)
        return pay
    elif inp == "2":
        v.info_dog()
        pay += 500
        buy(inp)
        return pay

def chbird():
    pay= 0
    print("1.Beo","\n2.Owl")
    inp=input("Choice the type :")
    if inp == "1":
        y.info_bird()
        pay += 300
        buy(inp)
        return pay
    elif inp == "2":
        b.info_bird()
        pay += 900
        buy(inp)
        return pay

def buy(inp):
    inp=input("Do you want to buy this pet? :")
    if inp == "y":
        print("You Purchased The Pet!! Thank You!!")
    return

def command(inp):
    if(inp == "cat"):
        return chcat()
    elif(inp == "dog"):
        return chdog()
    elif(inp == "bird"):
        return chbird()

def main():
    pay = 0
    while True:
        print(animals)
        inp=input("Choose Your Animals You Want :")
        paych = command(inp)
        pay += paych
        decision = input("Do you want to buy another pet? :")
        if decision == "n":
            break
    print("Thank you! And Please Come Again!")
    print("Total a Payment: $",(pay))


x=cat("Anggora","$500","Female","1 month")
c=cat("American","$600","Male","2 months")
z=dog("Husky","$800","male","3 months")
v=dog("Doge","$500","Female","3 months")
y=bird("Beo","$300","Female","2 months")
b=bird("Owl","$900","Male","4 months")

animals=["cat","dog","bird"]
main()




