from tkinter import *
import random
import time
import csv
import sys
from datetime import datetime
from pushover import init, Client

voornaam = str("")
achternaam= str("")
wachtwoord = str("")
vrijePlekken = 0
fietsnummer= 0
verify3 = str("")
test = ""
verify = 0
verschil2 = 0
prijs = 0

def infoalgemeen():
    bezet=0
    global vrijePlekken
    with open ('fietsen.csv','r') as file:
        for line in file:
            bezet += 1
        vrijePlekken = 1001 - bezet
    return vrijePlekken


def ophalen():
    global voornaam
    global wachtwoord
    global achternaam
    global fietsnummer
    global verify3
    global test
    global verify
    voornaam1 = voornaam.get()
    achternaam1 = achternaam.get()
    wachtwoord1 = wachtwoord.get()
    fietsnummer1 = fietsnummer.get()
    totallist= [fietsnummer1,voornaam1,achternaam1,wachtwoord1]
    verify = random.randrange(1000,9999)
    with open('fietsen.csv', 'r+') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if totallist == row[0:4]:
                with open('register.csv', 'r+') as file2:
                    reader = csv.reader(file2, delimiter=';')
                    for line in reader:
                        if totallist == line[0:4]:
                            print("homo")
                            test = 'Uw fiets staat klaar om opgehaald te worden. \nUw authenticatie code is:' +str(verify)+'\nWas u dit niet? Stuur dan een e-mail naar klantenservice@ns.nl\nWij hopen dat u van onze dienst heeft genoten en hopelijk tot ziens!'
                            init("atwfgt129b3q3ai4hh3nnmu23b2ebm")
                            Client("uqjs6boje6bp7okwnre9ndb7s2gwgs").send_message(test, title="NS Stalling")
    return test, verify


def inloggen():
    global voornaam
    global wachtwoord
    global achternaam
    global fietsnummer
    global v
    voornaam1 = voornaam.get()
    achternaam1 = achternaam.get()
    wachtwoord1 = wachtwoord.get()
    totallist = [fietsnummer,voornaam1,achternaam1,wachtwoord1]
    with open('register.csv','r') as file2:
        reader2 = csv.reader(file2, delimiter=';')
        for row in reader2:
            if totallist == row[0:4]:
                with open('fietsen.csv', 'r+') as file:
                    reader = csv.reader(file, delimiter=';')


def registercontrole():
    global voornaam
    global wachtwoord
    global achternaam
    global fietsnummer
    global v

    voornaam1 = voornaam.get()
    achternaam1 = achternaam.get()
    wachtwoord1 = wachtwoord.get()
    totallist = [fietsnummer,voornaam1,achternaam1,wachtwoord1]
    tijd=time.strftime("%Y-%m-%d %H:%M:%S")

    with open('register.csv','r') as file2:
        reader2 = csv.reader(file2, delimiter=';')
        for row in reader2:
            if totallist == row[0:4]:
                with open('fietsen.csv', 'r+') as file:
                    reader = csv.reader(file, delimiter=';')
                    for row in reader:
                        if str(fietsnummer) == row[0]:
                            sys.exit("De fiets met dit codenummer is al gestald")
                    total=(str(fietsnummer)+";"+voornaam1+";"+achternaam1+";"+wachtwoord1+";"+tijd+"\n")
                    file.writelines(total)


def verification():
    global test
    global verify3
    global v
    global verify

    verify2 = int(verify3.get())
    if verify == verify2:
        v.set("Uw fiets kan nu opgehaald worden!")
    else:
        v.set('Er is iets misgegaan, probeer opnieuw.')


def registreerWindow():
    root4 = Toplevel()

    global voornaam
    global wachtwoord
    global achternaam
    global v

    root4.geometry("500x500")
    root4.configure(background="yellow")

    titelLabel1 = Label(root4, text="Registreren, vul de volgende gegevens in", bg="yellow")
    titelLabel1.grid(columnspan=4)

    voorNaamLabel = Label(root4, text="Voornaam", bg="yellow")
    voorNaamLabel.grid(row=3, sticky=E)

    voornaam = Entry(root4)
    voornaam.grid(row=3, column=1)

    achterNaamLabel = Label(root4, text="Achternaam", bg="yellow")
    achterNaamLabel.grid(row=4, sticky=E)

    achternaam = Entry(root4)
    achternaam.grid(row=4, column=1)

    wachtwoordLabel = Label(root4, text="Wachtwoord", bg="yellow")
    wachtwoordLabel.grid(row=5, sticky=E)

    wachtwoord = Entry(root4)
    wachtwoord.grid(row=5, column=1)

    v = StringVar()
    fietsnummerLabel = Label(root4, textvariable=v, bg="yellow")
    fietsnummerLabel.grid(row=7, columnspan=2)

    submitButton = Button(root4, text='Submit', command=registreer)
    submitButton.grid(row=6, columnspan=2)

    quitButton = Button(root4, text="Sluit venster", command=root4.destroy)
    quitButton.grid(row=6, column=3, sticky=W)

    root4.mainloop()


def infoprive():
    global fietsnummer
    global wachtwoord
    global verschil2
    global prijs
    global h
    global g
    wachtwoord1 = wachtwoord.get()
    fietsnummer1 = fietsnummer.get()
    nu=time.strftime('%Y-%m-%d %H:%M:%S')
    with open ("fietsen.csv",'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if fietsnummer1 == row[0] and wachtwoord1 == row [3]:
                tijd=row[4]
                fmt = '%Y-%m-%d %H:%M:%S'
                d1 = datetime.strptime(str(tijd), fmt)
                d2 = datetime.strptime(str(nu), fmt)
                verschil=((d2-d1).seconds)
                verschil2=verschil/60
                verschil2=round(verschil2)
                prijs=round((verschil2*0.008333333),2)
                h.set(("Deze fiets staat "+str(verschil2)+" minuten in de stalling"))
                g.set(("De prijs van deze staltijd is "+str(prijs)+" euro."))
    return verschil2, prijs


def registreer():
    global voornaam
    global achternaam
    global wachtwoord
    global fietsnummer
    global v
    voornaam1 = voornaam.get()
    achternaam1 = achternaam.get()
    wachtwoord1 = wachtwoord.get()
    fietsnummer=str(random.randrange(0, 1000))
    with open('register.csv', 'r+') as file:
     reader = csv.reader(file, delimiter=';')
     for row in reader:
          while fietsnummer == row[0]:
              fietsnummer=str(random.randrange(0,9999999))
     total=str(fietsnummer+";"+voornaam1+";"+achternaam1+";"+wachtwoord1+'\n')
     file.writelines(total)
    v.set("Uw fietsnummer is: "+str(fietsnummer))
    registercontrole()
    return fietsnummer


def fietsOphalenWindow():
    root1 = Toplevel()

    global voornaam
    global wachtwoord
    global achternaam
    global fietsnummer
    global v
    global verify3

    root1.geometry("500x500")
    root1.configure(background="yellow")

    quitButton = Button(root1, text="Sluit venster", command=root1.destroy)
    quitButton.grid(row=6, column=3, sticky=W)

    titelLabel1 = Label(root1, text="Fiets ophalen, vul de volgende gegevens in", bg="yellow")
    titelLabel1.grid(row=0, columnspan=4)

    voorNaamLabel = Label(root1, text="Voornaam", bg="yellow")
    voorNaamLabel.grid(row=1, sticky=E)

    voornaam = Entry(root1)
    voornaam.grid(row=1, column=1)

    achterNaamLabel = Label(root1, text="Achternaam", bg="yellow")
    achterNaamLabel.grid(row=2, sticky=E)

    achternaam = Entry(root1)
    achternaam.grid(row=2, column=1)

    wachtwoordLabel = Label(root1, text="Wachtwoord", bg="yellow")
    wachtwoordLabel.grid(row=3, sticky=E)

    wachtwoord = Entry(root1)
    wachtwoord.grid(row=3, column=1)

    fietsnummerLabel = Label(root1, text="Fietsnummer", bg="yellow")
    fietsnummerLabel.grid(row=4, sticky=E)

    fietsnummer = Entry(root1)
    fietsnummer.grid(row=4, column=1)

    submitButton = Button(root1, text='Stuur verificatiecode', command=ophalen)
    submitButton.grid(row=5, columnspan=2)

    verifyCodeLabel = Label(root1, text="Verificatiecode", bg="yellow")
    verifyCodeLabel.grid(row=6, sticky=E)

    verify3 = Entry(root1)
    verify3.grid(row=6, column=1)

    verifyButton = Button(root1, text="Verify",command=verification)
    verifyButton.grid(row=7, columnspan=2)

    opgehaaldLabel = Label(root1, textvariable=v, bg="yellow")
    opgehaaldLabel.grid(row=8, columnspan=2)

    root1.mainloop()


def algemeneInfoWindow():
    root2 = Toplevel()
    global vrijePlekken

    root2.geometry("500x500")
    root2.configure(background="yellow")

    infoalgemeen()

    openingsTijd = Label(root2, text="De fietsenstalling is van 9 uur tot 23 uur geopend.", bg="yellow")
    openingsTijd.place(relx=0.2, rely=0.5, anchor=W)

    plekkenVrij = Label(root2, text="Er zijn nog " + str(vrijePlekken) + " plekken vrij.")
    plekkenVrij.place(relx=0.2, rely=0.45, anchor=W)

    stalKosten = Label(root2, text="Het stallen kost €0.50 per uur", bg="yellow")
    stalKosten.place(relx=0.2, rely=0.55, anchor=W)

    quitButton = Button(root2, text="Sluit venster", command=root2.destroy)
    quitButton.grid(row=6, column=3, sticky=W)

    root2.mainloop()


def priveInfoWindow():
    root3 = Toplevel()

    global wachtwoord
    global fietsnummer
    global h
    global g
    root3.geometry("500x500")
    root3.configure(background="yellow")

    infoLabel = Label(root3, text="Log in om prive informatie te kunnen inzien.", bg="yellow")
    infoLabel.grid(columnspan=4)

    fietsnummerLabel = Label(root3, text="Fietsnummer", bg="yellow")
    fietsnummerLabel.grid(row=1)

    fietsnummer = Entry(root3)
    fietsnummer.grid(row=1, column=1)

    wachtwoordLabel = Label(root3, text="Wachtwoord", bg="yellow")
    wachtwoordLabel.grid(row=2)

    wachtwoord = Entry(root3)
    wachtwoord.grid(row=2, column=1)

    loginButton = Button(root3, text="Login", command=infoprive)
    loginButton.grid(row=3, columnspan=2)

    tijdLabel = Label(root3, textvariable=h, bg="yellow")
    tijdLabel.grid(row=4, columnspan=2)

    prijsLabel = Label(root3, textvariable=g, bg="yellow")
    prijsLabel.grid(row=5, columnspan=2)

    wachtwoordLabel = Label(root3, text="Wachtwoord", bg="yellow")
    wachtwoordLabel.grid(row=2)
    root3.mainloop()

root = Tk()

h = StringVar()
v = StringVar()
g = StringVar()

root.geometry("500x500")
root.configure(background="yellow")
titelLabel = Label(root, text='yo')
titelLabel = Label(root, text='Fietsenstalling NS, maak uw keuze.', bg='yellow', font=20)
titelLabel.place(relx=0.5, rely=0.1, anchor=N)

stallenButton = Button(root, text='Registreren.', command=registreerWindow, bg='light blue', font=15)
stallenButton.place(relx=0.5, rely=0.35, anchor=CENTER)

ophalenButton = Button(root, text='Fiets ophalen.', command=fietsOphalenWindow, bg='light blue', font=15)
ophalenButton.place(relx=0.5, rely=0.5, anchor=CENTER)

algemeneInfoButton = Button(root, text='Algemene informatie opvragen.', command=algemeneInfoWindow, bg='light blue', font=15)
algemeneInfoButton.place(relx=0.5, rely=0.65, anchor=CENTER)

priveInfoButton = Button(root, text='Prive informatie opvragen.', command=priveInfoWindow, bg='light blue', font=15)
priveInfoButton.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
