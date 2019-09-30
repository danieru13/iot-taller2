import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import MySQLdb
import datetime

class AppFoto(tk.Frame):
  def __init__(self,master = None):
    super().__init__(master)
    # Configurando las dimensiones y el titulo de la ventana
    self.master.title('Login App')
    self.master.resizable(width=False, height=False)
    # Agregando el marco
    self.pack()

    # imagen
    self.img = ImageTk.PhotoImage(Image.open("foto.jpg"))

    # Agregando el label para la Foto
    self.photo = tk.Label(self, image = self.img)
    self.photo.pack(fill=tk.BOTH, expand=True)

    # Frame login
    self.loginFrame = tk.LabelFrame(self, text = "Login")
    self.loginFrame.pack(fill=tk.BOTH, expand=True)
    # Frame User
    self.frameUser = tk.Frame(self.loginFrame)
    self.frameUser.pack(fill=tk.BOTH, expand=True)
    self.labelUser = tk.Label(self.frameUser, width=9, \
                              justify = tk.LEFT, text = "User:")
    self.labelUser.pack(fill=tk.BOTH, expand=True, side = tk.LEFT)
    self.inputUser = tk.Entry(self.frameUser, text = "")
    self.inputUser.pack(fill=tk.BOTH, expand=True, side = tk.LEFT)
    # Pass login
    self.passFrame = tk.Frame(self.loginFrame)
    self.passFrame.pack(fill=tk.BOTH, expand=True)
    self.labelPass = tk.Label(self.passFrame, width=9, \
                              justify = tk.LEFT, text = "Password:")
    self.labelPass.pack(fill=tk.BOTH, expand=True, side = tk.LEFT)
    self.inputPass = tk.Entry(self.passFrame, show="*", text = "")
    self.inputPass.pack(fill=tk.BOTH, expand=True, side = tk.LEFT)
    # Button
    self.bLogin = tk.Button(self.loginFrame,text = "Login", command = self.login)
    self.bLogin.pack(fill=tk.BOTH, expand=True)

  def login(self):
    db = MySQLdb.connect(host="localhost", user="root",
    passwd="root", db="login")

    print("Logueando usuario!!!")
    u = self.inputUser.get()
    p = self.inputPass.get()

    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM usuarios WHERE nombre = '" + u + "' AND pass = '" + p + "'")
    
    if(res == 1):
        print(u)
        print(datetime.datetime.now())
        messagebox.showinfo("Bienvenido", "Ingreso exitoso")
    else:
        messagebox.showerror("Error", "Usuario y/o clave invalidos")    
if __name__ == "__main__":
  app = AppFoto()
  app.mainloop()