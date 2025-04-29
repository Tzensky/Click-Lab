from tkinter import *
import random
import time

unit = 100
listeCompetence = ["competence1","competence2","competence3"]

# Création de la fenêtre principale (Main Window)
fenetre = Tk()
fenetre.title('Rng - ClickLab')
fenetre.geometry('1280x720')
fenetre.resizable(width=False , height=False)

def nouveauLancer():
    if unit >= 100 :
        for i in range(10):
            texte.set(random.choice(listeCompetence))
            unit -= 100

    else :
        texte.set("Pas assez d'unit.")

boutonLancer = Button(fenetre, text ='Lancer - Prix 100', command = nouveauLancer).place(x= 500 , y= 300)

texte = StringVar()
labelLancer = Label(fenetre, textvariable = texte, fg ='Black', bg ='white').place(x= 500 , y= 280)



fenetre.mainloop()