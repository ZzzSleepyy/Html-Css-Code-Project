import customtkinter as ctk


window =  ctk.CTk()                                   
window.geometry("400x400")
window.title("Game")

ctk.set_appearance_mode("dark")


def function():
    label1 = ctk.CTkLabel(window, text="This is CTK")
    label1.pack()
    
button1 = ctk.CTkButton(window, text="Login", command=function, fg_color="#C0C0C0", font=("Times new roman",20))
button1.place(x=20,y=200)

entry1 = ctk.CTkEntry(window, placeholder_text="Password", show="*")
entry1.pack()



window.mainloop()

