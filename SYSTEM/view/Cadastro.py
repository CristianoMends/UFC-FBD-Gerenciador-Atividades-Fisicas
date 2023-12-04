import tkinter as tk
import tkinter.font as tkFont

class Cadastro:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_907=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_907["font"] = ft
        GLabel_907["fg"] = "#333333"
        GLabel_907["justify"] = "center"
        GLabel_907["text"] = "Cadastro de Usuario"
        GLabel_907.place(x=150,y=30,width=221,height=30)

        GLabel_395=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_395["font"] = ft
        GLabel_395["fg"] = "#333333"
        GLabel_395["justify"] = "left"
        GLabel_395["text"] = "Nome"
        GLabel_395.place(x=50,y=70,width=70,height=25)

        GLineEdit_50=tk.Entry(root)
        GLineEdit_50["bg"] = "#ffffff"
        GLineEdit_50["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_50["font"] = ft
        GLineEdit_50["fg"] = "#333333"
        GLineEdit_50["justify"] = "center"
        GLineEdit_50["text"] = ""
        GLineEdit_50.place(x=50,y=90,width=200,height=30)

        GLabel_76=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_76["font"] = ft
        GLabel_76["fg"] = "#333333"
        GLabel_76["justify"] = "center"
        GLabel_76["text"] = "Sobrenome"
        GLabel_76.place(x=50,y=120,width=70,height=25)

        GLineEdit_795=tk.Entry(root)
        GLineEdit_795["bg"] = "#ffffff"
        GLineEdit_795["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_795["font"] = ft
        GLineEdit_795["fg"] = "#333333"
        GLineEdit_795["justify"] = "center"
        GLineEdit_795["text"] = ""
        GLineEdit_795.place(x=50,y=140,width=200,height=30)

        GLabel_506=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_506["font"] = ft
        GLabel_506["fg"] = "#333333"
        GLabel_506["justify"] = "left"
        GLabel_506["text"] = "Usuario"
        GLabel_506.place(x=260,y=70,width=70,height=25)

        GLineEdit_946=tk.Entry(root)
        GLineEdit_946["bg"] = "#ffffff"
        GLineEdit_946["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_946["font"] = ft
        GLineEdit_946["fg"] = "#333333"
        GLineEdit_946["justify"] = "center"
        GLineEdit_946["text"] = ""
        GLineEdit_946.place(x=260,y=90,width=200,height=30)
        GLineEdit_946["show"] = "Usuario"

        GLabel_442=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_442["font"] = ft
        GLabel_442["fg"] = "#333333"
        GLabel_442["justify"] = "left"
        GLabel_442["text"] = "Senha"
        GLabel_442.place(x=260,y=120,width=70,height=25)

        GLineEdit_729=tk.Entry(root)
        GLineEdit_729["bg"] = "#ffffff"
        GLineEdit_729["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_729["font"] = ft
        GLineEdit_729["fg"] = "#333333"
        GLineEdit_729["justify"] = "center"
        GLineEdit_729["text"] = ""
        GLineEdit_729.place(x=260,y=140,width=200,height=30)

        GLabel_858=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_858["font"] = ft
        GLabel_858["fg"] = "#333333"
        GLabel_858["justify"] = "left"
        GLabel_858["text"] = "Nascimento"
        GLabel_858.place(x=50,y=180,width=70,height=25)

        GLineEdit_305=tk.Entry(root)
        GLineEdit_305["bg"] = "#ffffff"
        GLineEdit_305["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_305["font"] = ft
        GLineEdit_305["fg"] = "#333333"
        GLineEdit_305["justify"] = "center"
        GLineEdit_305["text"] = ""
        GLineEdit_305.place(x=50,y=200,width=100,height=25)

        GLabel_497=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "left"
        GLabel_497["text"] = "Peso"
        GLabel_497.place(x=50,y=230,width=70,height=25)

        GLineEdit_849=tk.Entry(root)
        GLineEdit_849["bg"] = "#ffffff"
        GLineEdit_849["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_849["font"] = ft
        GLineEdit_849["fg"] = "#333333"
        GLineEdit_849["justify"] = "center"
        GLineEdit_849["text"] = ""
        GLineEdit_849.place(x=50,y=250,width=100,height=25)

        GLabel_265=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_265["font"] = ft
        GLabel_265["fg"] = "#333333"
        GLabel_265["justify"] = "left"
        GLabel_265["text"] = "Altura"
        GLabel_265.place(x=50,y=290,width=70,height=25)

        GLineEdit_409=tk.Entry(root)
        GLineEdit_409["bg"] = "#ffffff"
        GLineEdit_409["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_409["font"] = ft
        GLineEdit_409["fg"] = "#333333"
        GLineEdit_409["justify"] = "center"
        GLineEdit_409["text"] = ""
        GLineEdit_409.place(x=50,y=310,width=99,height=25)

        GButton_849=tk.Button(root)
        GButton_849["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_849["font"] = ft
        GButton_849["fg"] = "#000000"
        GButton_849["justify"] = "center"
        GButton_849["text"] = "Finalizar"
        GButton_849.place(x=210,y=380,width=70,height=25)
        GButton_849["command"] = self.GButton_849_command

        GButton_977=tk.Button(root)
        GButton_977["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_977["font"] = ft
        GButton_977["fg"] = "#000000"
        GButton_977["justify"] = "center"
        GButton_977["text"] = "Cancelar"
        GButton_977.place(x=210,y=420,width=70,height=25)
        GButton_977["command"] = self.GButton_977_command

    def GButton_849_command(self):
        print("command")


    def GButton_977_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Cadastro(root)
    root.mainloop()
