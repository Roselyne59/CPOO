
prenom = input('Entrez votre prénom :')
age = input('Entrez votre age :')
print('{} a {} ans'.format(prenom, age))
prenom = 'Anyway'
age = 500
if prenom == 'Yoda' :
    print("Bonjour, Maître.")
elif age <= 500 :
    print("Ce n'est pas Yoda")
else :
    print("Mais vous êtes qui ??")