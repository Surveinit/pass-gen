from cgitb import text
from tkinter import *
from turtle import width
from pass_generator import *

window = Tk()
window.title("PassGen")
window.config(bg="#121212")
 
def gen():

    if(scale.get()==8):
        output = Label(text=pass_gen_e(),
                font=("impact",20), bg="#121212", fg="#ebebeb")
    
        output.pack()

    elif(scale.get()==10):
        output = Label(text=pass_gen(),
                font=("impact",20), bg="#121212", fg="#ebebeb")
    
        output.pack()

    else:
        output = Label(text=pass_gen_t(),
                font=("impact",20), bg="#121212", fg="#ebebeb")
    
        output.pack()

    

#heading
heading = Label(text="Pass-Generator",
                font=("impact",30), fg="#eb4034",bg="#121212")

heading.pack()
 

# Scale
scale = Scale(from_=8, to=12,
              orient=HORIZONTAL,
              tickinterval=2,
              resolution=2,
              showvalue=0,
              width=24)
scale.pack()


#Button

button = Button(command=gen,text="Generate",
                font=("impact",10),
                padx=19,  )

button.pack()


#Output 



window.mainloop()