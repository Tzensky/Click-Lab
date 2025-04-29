from tkinter import *
import random
import time
import tkinter.font as font

unit = 100
listeCompetence = ["competence1","competence2","competence3"]

# Création de la fenêtre principale (Main Window)
fenetre = Tk()
fenetre.title('Rng - ClickLab')
fenetre.geometry('1280x720')
fenetre.resizable(width=False , height=False)

def nouveauLancer():
    global unit
    if unit >= 100 :
        for i in range(10):
            texte.set(random.choice(listeCompetence))
        unit -= 100
    else :
        texte.set("Pas assez d'unit.")
        
f = font.Font(size= 20)

boutonLancer = Button(fenetre, text ='Lancer - Prix 100', command = nouveauLancer)
boutonLancer['font'] = f
boutonLancer.place(x= 620 , y= 370)

texte = StringVar()
texte.set("Bienvenue dans le shop de competence.")
labelLancer = Label(fenetre, textvariable = texte, fg ='Black', bg ='white')
labelLancer['font']=f
labelLancer.place(x= 630 , y= 350)



fenetre.mainloop()