import tkinter as tk
import tkinter.font as tkFont

class Comunidade:
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

        GLabel_678=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_678["font"] = ft
        GLabel_678["fg"] = "#333333"
        GLabel_678["justify"] = "center"
        GLabel_678["text"] = "Comunidade"
        GLabel_678.place(x=210,y=20,width=150,height=25)

        GLabel_758=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_758["font"] = ft
        GLabel_758["fg"] = "#333333"
        GLabel_758["justify"] = "center"
        GLabel_758["text"] = "Top 3 Usuario que utilizaram o maior peso"
        GLabel_758.place(x=20,y=60,width=152,height=30)

        GLabel_333=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_333["font"] = ft
        GLabel_333["fg"] = "#333333"
        GLabel_333["justify"] = "center"
        GLabel_333["text"] = "Top 3 Usuarios com maior numeros de registros"
        GLabel_333.place(x=20,y=240,width=139,height=30)

        GButton_756=tk.Button(root)
        GButton_756["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_756["font"] = ft
        GButton_756["fg"] = "#000000"
        GButton_756["justify"] = "center"
        GButton_756["text"] = "Voltar"
        GButton_756.place(x=280,y=450,width=70,height=25)
        GButton_756["command"] = self.GButton_756_command

        GListBox_44=tk.Listbox(root)
        GListBox_44["bg"] = "#ffffff"
        GListBox_44["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_44["font"] = ft
        GListBox_44["fg"] = "#333333"
        GListBox_44["justify"] = "center"
        GListBox_44.place(x=200,y=100,width=80,height=25)

        GListBox_100=tk.Listbox(root)
        GListBox_100["bg"] = "#ffffff"
        GListBox_100["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_100["font"] = ft
        GListBox_100["fg"] = "#333333"
        GListBox_100["justify"] = "center"
        GListBox_100.place(x=200,y=290,width=80,height=25)

        GLineEdit_364=tk.Entry(root)
        GLineEdit_364["bg"] = "#ffffff"
        GLineEdit_364["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_364["font"] = ft
        GLineEdit_364["fg"] = "#333333"
        GLineEdit_364["justify"] = "left"
        GLineEdit_364["text"] = ""
        GLineEdit_364.place(x=20,y=100,width=142,height=117)

        GLineEdit_12=tk.Entry(root)
        GLineEdit_12["bg"] = "#ffffff"
        GLineEdit_12["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_12["font"] = ft
        GLineEdit_12["fg"] = "#333333"
        GLineEdit_12["justify"] = "left"
        GLineEdit_12["text"] = ""
        GLineEdit_12.place(x=20,y=290,width=142,height=135)

    def GButton_756_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Comunidade(root)
    root.mainloop()