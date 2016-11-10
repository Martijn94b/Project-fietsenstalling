from tkinter import *
import random
import time
import csv
import sys
from datetime import datetime

voornaam = str("")
achternaam= str("")
wachtwoord = str("")
vrijePlekken = 0
fietsnummer= 0
v = ""

def infoalgemeen():
    bezet=0
    global vrijePlekken
    with open ('fietsen.csv','r') as file:
        for line in file:
            bezet += 1
        vrijePlekken = 1001 - bezet
    return vrijePlekken

def fietsStallenWindow():
    root4 = Toplevel()

    global voornaam
    global wachtwoord
    global achternaam
    global v

    root4.geometry("500x500")
    root4.configure(background="yellow")

    titelLabel1 = Label(root4, text="Fiets stallen, vul de volgende gegevens in", bg="yellow")
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

    quitButton = Button(root4, text="Quit", command=root4.destroy)
    quitButton.grid(row=6, column=3, sticky=W)

    root4.mainloop()

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

    print ('-uw fietsnummer is '+fietsnummer)
    v.set("Uw fietsnummer is: "+str(fietsnummer))
    return fietsnummer

def fietsOphalenWindow():
    root1 = Toplevel()

    root1.geometry("500x500")
    root1.configure(background="yellow")

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

    root2.mainloop()

def priveInfoWindow():
    root3 = Toplevel()

    root3.geometry("500x500")
    root3.configure(background="yellow")

    infoLabel = Label(root3, text="Log in om prive informatie te kunnen inzien.")
    infoLabel.place()
    wwLabel = Label(root3, text="wachtwoord")
    wwLabel.place(relx=0.2, rely=0.5, anchor=E)
    wachtwoord = Entry(root3)
    wachtwoord.place(relx=0.25, rely=0.5, anchor=W)

    root3.mainloop()

root = Tk()

root.geometry("500x500")
root.configure(background="yellow")
titelLabel = Label(root, text='yo')
titelLabel = Label(root, text='Fietsenstalling NS, maak uw keuze.', bg='yellow', font=20)
titelLabel.place(relx=0.5, rely=0.1, anchor=N)

stallenButton = Button(root, text='Fiets stallen.', command=fietsStallenWindow, bg='light blue', font=15)
stallenButton.place(relx=0.5, rely=0.35, anchor=CENTER)

ophalenButton = Button(root, text='Fiets ophalen.', command=fietsOphalenWindow, bg='light blue', font=15)
ophalenButton.place(relx=0.5, rely=0.5, anchor=CENTER)

algemeneInfoButton = Button(root, text='Algemene informatie opvragen.', command=algemeneInfoWindow, bg='light blue', font=15)
algemeneInfoButton.place(relx=0.5, rely=0.65, anchor=CENTER)

priveInfoButton = Button(root, text='Prive informatie opvragen.', command=priveInfoWindow, bg='light blue', font=15)
priveInfoButton.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
