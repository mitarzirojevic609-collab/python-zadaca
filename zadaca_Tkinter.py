import tkinter as tk
import re

window = tk.Tk() #NAPRAVIO NOVI PROZOR(WINDOW)
window.geometry("1024x720") #dimenzije
window.title("moj program")

is_dark_mode = True

window.configure(bg="black")

#Creating main label
tk.Label(window,
         text="Poyyyy",
         font= ("Arial", 16),
         fg="darkblue",
         bg="orange"

).pack()

#======== Sing up button =======
def on_click():

    email = email_entry.get()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email) is None:
        print("Uneti mejl nije u dobrom formatu")

    if email == "admin@admin.com" and password_entry.get() == "123456":
        print("dobrodosao")
    else:
        print("pogresni kredicijali!")

def change_color():
    global is_dark_mode

    if is_dark_mode:
        is_dark_mode = False
        window.configure(bg="white")
    else:
        is_dark_mode = True
        window.configure(bg="black")





tk.Button(window,
          text="Sing Up",
          font=("Arial", 16),
          bg="darkblue",
          fg="white",
          command=on_click
).pack(pady=15)

tk.Button(window,
          text="Change collor",
          font=("Arial", 16),
          bg="darkblue",
          fg="white",
          command=change_color
).pack(pady=15)





#======== Entry =======
password_entry = tk.Entry(window, width=50)
password_entry.pack()

#====== Email Entry =====
email_entry = tk.Entry(window, width=50)
email_entry.pack()





window.mainloop()  # pokreni prozor koji je napravljen