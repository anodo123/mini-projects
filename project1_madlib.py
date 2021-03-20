from tkinter import *
root= Tk()
root.geometry("300x300")
root.title("Mad lib")
#Label(root,text="datalib",font="arial20bold").pack()
#Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)
def madlib():
    place=str(input("Enter a place"))
    food=str(input("Enter a food"))
    hairstyles=str(input("Enter a hairstyles"))
    animals=str(input("Enter an animal"))
    cars=str(input("Enter an car"))
    print("The "+place+" is a wierd place people there have ugly "+food+ " ugly "+hairstyles+" ugly "
          +animals+" even the "+ cars+ " were ugly, Ive never thought i would have gone to The "+place +" will be stuck in my mind forever.")
canvas = Canvas(root)
canvas.pack()
Madlib=madlib()
root.mainloop()
