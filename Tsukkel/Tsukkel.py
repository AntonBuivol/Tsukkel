#for
#n=int(input("Kirjuta mingi täisarv: "))
#summ=1
#for x in range(1,n):
#    summ+=x*summ
#print("See on faktoriaal: ",summ)


#while
#n=int(input("Kirjuta mingi täisarv: "))
#summ=1
#x=0
#while x<n:
#    summ+=x*summ
#    x+=1
#print("See on faktoriaal: ",summ)
    


#4
#for variant
#for x in range(1,11):
#        print(x)
#print()
#for x in range(1,11):
#    for y in range(1,11):
#        print(x*y, end=" ")
#    print()


#while variant
#a=1
#while a<=10:
#        print(a)
#        a+=1
#print()
#x=1
#while x<=10:
#    y=1
#    while y<=10:
#        print(x*y, end=" ")
#        y+=1
#    print(" ")
#    x+=1


#while True variant
#a=1
#while True:
#    print(a)
#    a+=1
#    if a == 11:
#        break
#print()
#x=1
#while True:
#    y=1
#    s=""
#    if x<=10:
#        while True:
#            if y<=10:
#                s+=str(x*y)+" "
#            else:
#                break
#            y+=1
#    else:
#        break
#    x+=1
#    print(s)
#    print()


#6
#print()
#for i in range(0,5):
#    print("* "*5)
#print()
#for i in range(0,10):
#    print("* "*i)
#print()
#for i in range(0,10):
#    print("* "(10-i))
#print()


#8
#while True:
#    try:
#        mainnumber=int(input("Vali number 1-100: "))
#        break
#    except ValueError:
#        print("See pole täisarv")
#if mainnumber<1 or mainnumber>100:
#    print("Vali õige number")
#else:
#    paaris=0
#    paaritu=0
#    x=0
#    while x!=mainnumber:
#        x=x+1
#        print(int(x),end=" ")
#        if x%2==0:
#            paaris+=1
#        else:
#            paaritu+=1

#print("Paaris numbrid: ",paaris)
#print("Paaritu numbrid: ",paaritu)


#10
#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:
#        print(x, end=" ")
#        x+=1

#x=1
#while x<=100:
#    if x%5==0:
#        print(x, end=" ")
#        x+=1

#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end=" ")

#x=0
#while True:
#    if x==50:
#        break
#    elif x%2==1:
#        print()


#11
#from random import*

#x=0
#n=randint(1,10)
#while True:
#    text=input("Väli jumiseks sisestage number: ")
#    x+=1
#    if text=="stopp":
#        print("Välju programmist! Kohtuminseni! See sai tehtud ",n)
#        break
#    elif int(text)==n:
#        print("Palju õnne, sa võitsid!")
#        break
#    elif x==3:
#        print("Oli 3 katse")
#        break


#13
#for variant
#print("arv", " ruut ", "  kuup")
#for i in range(1,11):
#    print(f"{i}   {i**2}   {i**3}")
#print("teine variant")

#while variant
#print("arv", " ruut ", "  kuup")
#i=1
#while i<11:
#    print(f" {i}   {i**2}   {i**3}")
#    i=1


#16
#from random import random

#ans = random.randint(1, 10)
#while True:
#    g=input("Mis numbri ma arvatasin?(1-10, mängu lõpetamiseks kirjutage *lõpp* ) \n")
#    if g.lower() == "lõpp":
#        print("mäng on läbi!")
#        break
#    if not g.isnumeric():
#        print("Vale andmetüüp!")
#        continue
#    g=int(g)
#    if g>10 or g<1:
#        print("Vahemik on vale")
#        continue
#    elif g!=ans:
#        print(f"vale! proovi veel korral!")
#        continue


#17
#from random import random
#try:
#    num_horiz=int(input("Sisesta ruutude arv horizontaalne: "))
#except:
#    print("Value error")
#    num_horiz=randint(1,10000)
#try:
#    num_vert=int(input("Sisesta ruutude arv vertikaalne: "))
#except:
#    print("Value error")
#    num_vert=randint(1,10000)

#for y in range(num_vert):
#    for x in range(num_horiz):
#        print("¤", end=" ")
#    print()


#a=random.randint(1,100)

#b=0

#while b!=a:
#    try:
#        b=int(input("Uess mõistatuse number vahemikus 1-100: "))
#        if b>100 or b<1:
#            print("Vahemik on vale")
#        if b<a:
#            print("Liiga väike: Proovi uuseti.")
#        if b>a:
#            print("Liiga suur: Proovi uuesti.")
#        else:
#            print("Palju õnne: Sa arvasid misteeriumi ära.", a)
#            break
#    except:
#        print("Value error")


#3
#from random import randint

#try:
#    f=int(input("Mitu algarvu sa tahad? "))
#    for d in range(0,f,1):
#        print("Ülesanne")
#        a=randint(1,50)
#        b=randint(1,50)
#        c=a+b
#        for i in range (0,5,1):
#            answer=int(input(f"{a}+{b}=? "))
#            if answer==a+b:
#                print("See on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        print(f"Õige on {c} ")
#except:
#    print("See ei ole õige")


#22
#n=1
#while True:
#    print("Tahan kommi!")
#    a=str(input())
#    if a=="komm" or a=="KOMM"
#        print("Aitäh! Oli väga"+str(n)+" katse ")
#        break
#    else:
#        n=n+1


#import string
#import random
#print("Guess letter - (From Aa to Zz)")
#letter=random.choice(string.ascii_letters)

#while True:
#    answ=str(input("Your guess: "))
#    if letter==answ:
#        print("Good job!")
#        break
#    else:
#        print("Try again!")
