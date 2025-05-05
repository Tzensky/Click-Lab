from tkinter import *
from PIL import Image, ImageTk
import time
import threading


fn = Tk()
fn.title("Calculatrice")
fn.geometry("1280x720")
fn.resizable(width=False, height=False)
 
# j'ai modifié le nom du fichier
# pour tester de mon côté
image = Image.open("fiole.png")
photo = ImageTk.PhotoImage(image)
   
# canvas plus grand que l'image
# (j'ai pris une image qui fait 225 x 225 px)
canvas = Canvas(fn, width=600, height=500)
canvas.pack()
 
# je place l'image au pif à peu près au centre du canvas
# et on lui ajoute un tag (voir fonction coords dans la
# fonction detect_clic)
cookie = canvas.create_image(190, 100, anchor=NW, image=photo, tags="cookie")
           
compteur_click = 0


def compte_click(event):
    global compteur_click
    x , y = event.x, event.y
    # renvoie la position de l'image sous la forme [x, y] :
    fiole_coords = canvas.coords("cookie")
 
    # détection du clic sur l'image :
    if x >= fiole_coords[0] and x <= fiole_coords[0] + image.size[0]:
        if y >= fiole_coords[1] and y <= fiole_coords[1] + image.size[1]:
            compteur_click += 1
            texte.set(compteur_click)
   
   
# Création d'un widget Label (texte 'Résultat -> x')
texte = StringVar()
labelResultat = Label(fn, text = "Nombre de clicks :", textvariable = texte, fg ='black', bg ='white').place(x=100, y=0)
   
Button(fn,text="Lootbox",command=fn.destroy).place(x=100,y=400)
Button(fn,text="Lootbox",command=fn.destroy).place(x=430,y=400)
Button(fn,text="Nombre de click :",command=compte_click).place(x=0,y=400)



canvas.bind("<Button-1>",compte_click)
 
fn.mainloop()
