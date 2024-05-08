#import packages 
import tkinter as tk
import webbrowser
#define functions
def instagram(event):
    webbrowser.open_new_tab('https://www.instagram.com/charan_.i')
def Linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/nagacharan-g')
def Github(event):
    webbrowser.open_new_tab('https://www.github.com/charan-happy')

# window for the app

window=tk.Tk()
window.geometry("300x200")
window.title("Social Media Bookmark App")

# label creation

label1 = tk.Label(text="My Social Media")
label1.grid(column=10, row=10)

# styling labell
label1= tk.Label(text = "My Social Media", font=("Times new roman", 200))

# create three buttons each for Instagram, Linkedin, Github. Arrange them using the 'grid' method. 
# To change colours we use 'bg' argument.

button1=tk.Button(window,text="Instagram", bg='orange')
button1.grid(column=500,row=120)
button2=tk.Button(window,text="Linkedin", bg="blue")
button2.grid(column=700,row=200)
button3=tk.Button(window,text="Github",bg="White")
button3.grid(column=900, row=260)

#binding to their corresponding functions

button1.bind("<Button-1>", instagram)
button2.bind("<Button-1>",Linkedin)
button3.bind("<Button-1>",Github)

#run using mainloop method
window.mainloop()
