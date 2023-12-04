import tkinter as tk
import tkinter.font as tkFont

class Selecao:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_247=tk.Button(root)
        GButton_247["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_247["font"] = ft
        GButton_247["fg"] = "#000000"
        GButton_247["justify"] = "center"
        GButton_247["text"] = "Treino"
        GButton_247.place(x=240,y=170,width=100,height=25)
        GButton_247["command"] = self.GButton_247_command

        GLabel_120=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_120["font"] = ft
        GLabel_120["fg"] = "#333333"
        GLabel_120["justify"] = "center"
        GLabel_120["text"] = "Veja treinos de outros usuarios."
        GLabel_120.place(x=360,y=110,width=150,height=25)

        GLabel_496=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "#333333"
        GLabel_496["justify"] = "left"
        GLabel_496["text"] = "Registre seus treinos."
        GLabel_496.place(x=360,y=170,width=150,height=25)

        GButton_351=tk.Button(root)
        GButton_351["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_351["font"] = ft
        GButton_351["fg"] = "#000000"
        GButton_351["justify"] = "center"
        GButton_351["text"] = "Perfil"
        GButton_351.place(x=240,y=230,width=100,height=25)
        GButton_351["command"] = self.GButton_351_command

        GLabel_679=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_679["font"] = ft
        GLabel_679["fg"] = "#333333"
        GLabel_679["justify"] = "left"
        GLabel_679["text"] = "Veja seu perfil"
        GLabel_679.place(x=360,y=230,width=150,height=25)

        GLabel_631=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_631["font"] = ft
        GLabel_631["fg"] = "#333333"
        GLabel_631["justify"] = "center"
        GLabel_631["text"] = "Olá 'Usuario' , Bem vindo!"
        GLabel_631.place(x=180,y=30,width=250,height=25)

        GButton_534=tk.Button(root)
        GButton_534["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_534["font"] = ft
        GButton_534["fg"] = "#000000"
        GButton_534["justify"] = "center"
        GButton_534["text"] = "Comunidade"
        GButton_534.place(x=240,y=110,width=100,height=25)
        GButton_534["command"] = self.GButton_534_command

    def GButton_247_command(self):
        print("command")


    def GButton_351_command(self):
        print("command")


    def GButton_534_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Selecao(root)
    root.mainloop()
