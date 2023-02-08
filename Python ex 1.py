
nom=input("Ecrivez votre nom :")
print("Votre nom est :", nom)
prenom=input("Ecrivez votre prenom :")
print("Votre prenom est :", prenom)
age=input("Ecrivez votre age :")
print("Vous avez :  ", age,"ans")

if int(age) == 9 or int(age) == 10 :
    print("Vous etes Poussin")
elif int(age) == 11 or int(age) == 12 :
    print("Vous etes Benjamin")
elif int(age) == 13 or int(age) == 14 :
    print("Vous etes Minime")
elif int(age) == 15 or int(age) == 16 :
    print("Vous etes Cadet")
elif int(age) == 17 or int(age) == 18 :
    print("Vous etes Junior")
elif int(age) >= 19 or int(age) <= 34 : 
    print("Vous etes Senior")
else :
    print("Vous etes veteran")



