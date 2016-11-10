#fietsen.csv  = gestalde fietsen
#register= naameigenaar+ nummerfiets= register.csv
import random
import time
import csv
import sys
from datetime import datetime

#---Registreren
def registreer():
    naam=input("Voer uw voornaam in: ")
    achternaam=input("Voer uw achternaam in: ")
    fietsnummer=str(random.randrange(0,9999999))
    wachtwoord=str(input("Vul een nieuwe PIN-Code in: "))
    stalling=str(0)
    with open('register.csv', 'r+') as file:
     reader = csv.reader(file, delimiter=';')
     for row in reader:
          while fietsnummer == row[0]:
              fietsnummer=str(random.randrange(0,9999999))
     total=str(fietsnummer+";"+naam+";"+achternaam+";"+wachtwoord+";"+stalling+'\n')
     file.writelines(total)

    print ('-uw fietsnummer is '+fietsnummer)


#---Stallen met eerst controle in register
def registercontrole():
    naam=input("Voer uw naam in: ")
    achternaam=input("Voer uw achternaam in: ")
    fietsnummer=(input("Voer uw fietsnummer in: "))
    wachtwoord=str(input("Voer uw PIN-Code in: "))
    totallist= [fietsnummer,naam,achternaam,wachtwoord]
    tijd=time.strftime("%Y-%m-%d %H:%M:%S")
    with open('register.csv','r') as file2:
        reader2 = csv.reader(file2, delimiter=';')
        for row in reader2:
            if totallist == row[0:4]:
                #fiets stallen
                with open('fietsen.csv', 'r+') as file:
                    reader = csv.reader(file, delimiter=';')
                    for row in reader:
                        if str(fietsnummer) == row[0]:
                            sys.exit("De fiets met dit codenummer is al gestald")
                    total=(str(fietsnummer)+";"+naam+";"+achternaam+";"+wachtwoord+";"+tijd+"\n")
                    file.writelines(total)
                sys.exit("Uw fiets is nu gestald")
        sys.exit('fiets is niet geregistreerd')

#---Informatie opvragen
def infoalgemeen():
    bezet=0
    with open ('fietsen.csv','r') as file:
        for line in file:
            bezet+=1
        vrijeplekken= 1000- bezet

    tijd=time.strftime("%X ")
    print('\n'+'De fietsenstalling is van 9 uur tot 23 uur geopend.' )
    print('De tijd is nu '+tijd)
    print('er zijn nog '+str(vrijeplekken)+' plekken vrij.')
    print('het stallen kost 50 cent per uur.')
#---Geef staltijd weer/priveinfo
def infoprive():
    fietsnummer=str(input("Wat is uw fietsnummer: "))
    wachtwoord=str(input("Voer uw PIN-code in: "))
    nu=time.strftime('%Y-%m-%d %H:%M:%S')
    with open ("fietsen.csv",'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if fietsnummer == row[0] and wachtwoord == row [3]:
                tijd=row[4]
                fmt = '%Y-%m-%d %H:%M:%S'
                d1 = datetime.strptime(str(tijd), fmt)
                d2 = datetime.strptime(str(nu), fmt)
                verschil=((d2-d1).seconds)
                verschil2=verschil/60
                verschil2=round(verschil2)
                prijs=round((verschil2*0.008333333),2)
                print ("Deze fiets staat "+str(verschil2)+" minuten in de stalling")
                print ("De prijs van deze staltijd is "+str(prijs)+" euro.")
                sys.exit()
        sys.exit("Deze gegevens zijn incorrect")

#---Fiets ophalen
def ophalen():
    naam=input("Voer uw naam in: ")
    achternaam=input("Voer uw achternaam in: ")
    fietsnummer=(input("Voer uw fietsnummer in: "))
    wachtwoord=input("Voer uw PIN-code in: ")
    totallist= [fietsnummer,naam,achternaam,wachtwoord]
    with open('fietsen.csv', 'r+') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if totallist == row[0:4]:
                with open('register.csv', 'r+') as file2:
                    reader = csv.reader(file2, delimiter=';')
                    writer=csv.writer(file2, delimiter=";")
                    for line in reader:
                        if totallist == line[0:4]:
                            test = 'Uw fiets is zojuist uit de stalling verwijderd. \nWas u dit niet? Stuur dan een e-mail naar klantenservice@ns.nl\nWij hopen dat u van onze dienst heeft genoten en hopelijk tot ziens!'
                            from pushover import init, Client

                            init("atwfgt129b3q3ai4hh3nnmu23b2ebm")
                            Client("uqjs6boje6bp7okwnre9ndb7s2gwgs").send_message(test, title="NS Stalling")





                print ("Uw fiets is nu opgehaald")
            else:
                print('kon fiets niet ophalen')

#---Keuzemenu
keuze =0
keuzelist=[1,2,3,4,5,6]
while keuze not in keuzelist:
    try:
        print('Dit is het keuzemenu: ')
        print('-1: Fiets registreren')
        print('-2: Fiets stallen')
        print('-3: Algemene informatie opvragen')
        print('-4: Prive informatie opvragen')
        print('-5: Ik wil mijn fiets ophalen')
        print('-6: Ik wil stoppen')
        keuze=int(input("Maak een keuze uit de getallen 1-6: "))
    except:
        print('Gebruik GETALLEN ')

    if keuze == 1:
        registreer()
    elif keuze ==2:
        registercontrole()
    elif keuze ==3:
        infoalgemeen()
    elif keuze == 4:
        infoprive()
    elif keuze == 5:
        ophalen()
    elif keuze == 6:
        sys.exit('Tot ziens!')

