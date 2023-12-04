from view.login import Login
import tkinter as tk



login = Login()

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
