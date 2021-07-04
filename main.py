from tkinter import *
from tkinter import ttk
from typing import Iterable
import os
from tkinter import messagebox
import json
import hashlib
from pickle import load, dump
import re
import base64
from urllib.request import urlretrieve
import json


class App(Tk):
    def __init__(self, title: str, size: Iterable[int], resizable: Iterable, *args, **kwargs):
        self.window = Tk.__init__(self, *args, **kwargs)
        self.size = size
        self.title(title)
        self.resizable(*resizable)
        self.geometry(f'{self.size[0]}x{self.size[1]}')
        self.config(bg='#1f1f1f')
        self.search_icon = urlretrieve('https://johnsdb.cleverapps.io/images/search.gif', 'Search.gif')
        self.add_icon = urlretrieve('https://johnsdb.cleverapps.io/images/add.gif', 'Add.gif')
        self.try_icon = urlretrieve('https://johnsdb.cleverapps.io/images/try.gif', 'Try.gif')
        self.list_icon = urlretrieve('https://johnsdb.cleverapps.io/images/list.gif', 'List.gif')
        self.app_icon = urlretrieve('https://johnsdb.cleverapps.io/images/icon.ico', 'Icon.ico')

    def calculator(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry('420x350')
        self.window.protocol('WM_DELETE_WINDOW', self.reveal)

        txtBox = Entry(self.window, fg='purple', justify='right', font=('Constantia', 20), width=19)
        txtBox.place(x=86, y=15)

        def Button_Clicked(whichClick):
            txtBox.insert("end", whichClick)
            
        def Calc_Equation():
            try:
                sEquation = str(txtBox.get())
                txtBox.delete(0, "end")
                sEquation = eval(sEquation)
                txtBox.insert(0, sEquation)
            except ZeroDivisionError:
                txtBox.delete(0, "end")
                txtBox.insert(0, "Cannot Divide By Zero")
                
        def Clear_Box():
            txtBox.delete(0, "end")        
            
        btnOne = Button(self.window, text='1', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(1))
        btnOne.place(x=10, y=70)
        btnTwo = Button(self.window, text='2', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(2))
        btnTwo.place(x=60, y=70)
        btnThree = Button(self.window, text='3', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(3))
        btnThree.place(x=110, y=70)
        btnFour = Button(self.window, text='4', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(4))
        btnFour.place(x=10, y=120)
        btnFive = Button(self.window, text='5', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(5))
        btnFive.place(x=60, y=120)
        btnSix = Button(self.window, text='6', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(6))
        btnSix.place(x=110, y=120)
        btnSeven = Button(self.window, text='7', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(7))
        btnSeven.place(x=10, y=170)
        btnEight = Button(self.window, text='8', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(8))
        btnEight.place(x=60, y=170)
        btnNine = Button(self.window, text='9', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(9))
        btnNine.place(x=110, y=170)
        btnZero = Button(self.window, text='0', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked(0))
        btnZero.place(x=60, y=220)
            
        btnPlus = Button(self.window, text='+', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked("+"))
        btnPlus.place(x=280, y=70)
        btnMinus = Button(self.window, text='-', font=('Constantia',15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked("-"))
        btnMinus.place(x=330, y=70)
        btnMultiply = Button(self.window, text='*', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked("*"))
        btnMultiply.place(x=280, y=120)
        btnDivide = Button(self.window, text="/", font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Button_Clicked("/"))
        btnDivide.place(x=330, y=120)
        btnEqual = Button(self.window, text="=", font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Calc_Equation())
        btnEqual.place(x=280, y=170)
            
        btnClear = Button(self.window, text='c', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda: Clear_Box())
        btnClear.place(x=330, y=170)

    def todo(self):
        self.window = Tk()
        self.window.title("To-Do List by @TokyoEdtech")
        self.window.protocol('WM_DELETE_WINDOW', self.reveal)

        def add_task():
            task = entry_task.get()
            if task != "":
                listbox_tasks.insert(END, task)
                entry_task.delete(0, END)
            else:
                messagebox.showwarning(title="Warning!", message="You must enter a task.")

        def delete_task():
            try:
                task_index = listbox_tasks.curselection()[0]
                listbox_tasks.delete(task_index)
            except:
                messagebox.showwarning(title="Warning!", message="You must select a task.")

        def load_tasks():
            try:
                tasks = load(open("tasks.dat", "rb"))
                listbox_tasks.delete(0, END)
                for task in tasks:
                    listbox_tasks.insert(END, task)
            except:
                messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

        def save_tasks():
            tasks = listbox_tasks.get(0, listbox_tasks.size())
            dump(tasks, open("tasks.dat", "wb"))

        # Create GUI
        frame_tasks = Frame(self.window)
        frame_tasks.pack()

        listbox_tasks = Listbox(frame_tasks, height=10, width=50)
        listbox_tasks.pack(side=LEFT)

        scrollbar_tasks = Scrollbar(frame_tasks)
        scrollbar_tasks.pack(side=RIGHT, fill=Y)

        listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=listbox_tasks.yview)

        entry_task = Entry(self.window, width=50)
        entry_task.pack()

        button_add_task = Button(self.window, text="Add task", width=48, command=add_task)
        button_add_task.pack()

        button_delete_task = Button(self.window, text="Delete task", width=48, command=delete_task)
        button_delete_task.pack()

        button_load_tasks = Button(self.window, text="Load tasks", width=48, command=load_tasks)
        button_load_tasks.pack()

        button_save_tasks = Button(self.window, text="Save tasks", width=48, command=save_tasks)
        button_save_tasks.pack()
    
    def login(self):
        global password
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.resizable(False, False)
        self.window.protocol('WM_DELETE_WINDOW', self.reveal)
        self.state = { "text": "Login to access password database.", "val": False }

        try:
            password = open("pwd", "r").read()
        except IOError:
            pass
        
        def addConfigBtn(login):
            btnList = ["Add", "List", "Search"]
            btnCmdList = [lambda: AddWindow(self.window), lambda: ListWindow(self.window), lambda: SearchWindow(self.window)]
            f = []
            img = []
            self.temp = []

            for i in range(3):
                f.append(Frame(self.window, padx=2, width=50, height=50))
                # f[i].grid(row=3, column=i)
                f[i].pack(side=LEFT, padx=0 if i else (50, 0))
                img.append(PhotoImage(file=btnList[i] + ".gif", width=48, height=48, master=self.window))
                self.temp.append(img[i])
                ttk.Button(f[i], image=img[i], text=btnList[i], compound="top", style="Submit.TButton", command=btnCmdList[i]).grid(sticky="NWSE")

        def checkPwd(frame, **kwargs):
            chk = kwargs['entry'].get()
            if hashlib.md5(chk.encode()).hexdigest() == password:
                self.state['text'] = "Logged In"
                self.state['val'] = True
                kwargs['label'].config(text=self.state['text'])
                kwargs['entry'].config(state=DISABLED)
                kwargs['btn'].config(state=DISABLED)
                addConfigBtn(frame)
            else:
                kwargs['label'].config(text=self.state['text'] + "\nTry Again!!!")


        def addLoginFrame(*kwargs):
            login = Frame(self.window, padx=2, pady=2, bd=2)
            login.pack()

            loginLabel = Label(login, text=self.state['text'], bd=10, font=LARGE_FONT, width=30)
            loginLabel.grid(row=0, columnspan=3)

            entry = ttk.Entry(login, show="*")
            entry.grid(row=1, column=1, pady=3)
            entry.bind('<Return>', lambda _: checkPwd( login, label=loginLabel, entry=entry, btn=submitBtn))
            entry.focus_set()

            s = ttk.Style()
            s.configure("Submit.TButton", font=BUTTON_FONT)
            submitBtn = ttk.Button(login, text="Submit", style="Submit.TButton", command=lambda: checkPwd( login, label=loginLabel, entry=entry, btn=submitBtn))

            submitBtn.grid(row=2, column=1, pady=3)
        
        
        def register(frame, *pwd):
            global password
            if pwd[0].get() == pwd[1].get():
                password = hashlib.md5(pwd[0].get().encode()).hexdigest()
                open("pwd", "w").write(password)

                frame.destroy()
                addLoginFrame()
            else:
                error = "Passwords dont match!!\nTry again."
                errorLabel = Label(frame, text=error, bd=10, font=("Verdana", 11), fg="red")
                errorLabel.grid(row=4, column=1, pady=3)
                for wid in pwd:
                    wid.delete(0, 'end')

        self.register = register
        def addRegisterFrame(*arg):
            register = Frame(self.window, padx=2, pady=2, bd=2)
            register.pack()

            info = "Register with a password\nTo start using the manager"
            registerLabel = Label(register, text=info, bd=10, font=LARGE_FONT, width=30)
            registerLabel.grid(row=0, columnspan=3)

            entry = ttk.Entry(register, show="*")
            entry.grid(row=1, column=1, pady=3)
            entry.focus_set()

            entryChk = ttk.Entry(register, show="*")
            entryChk.grid(row=2, column=1, pady=3)
            entryChk.bind('<Return>', lambda _: self.register(register, entry, entryChk))

            s = ttk.Style()
            s.configure("Submit.TButton", font=BUTTON_FONT)
            submitBtn = ttk.Button(register, text="Register", style="Submit.TButton", command=lambda: self.register(register, entry, entryChk))
            submitBtn.grid(row=3, column=1, pady=3)

        
        if password:
            addLoginFrame()
        else:
            addRegisterFrame()
    
    def editor(self):
        self.window = Tk()
        self.window.protocol('WM_DELETE_WINDOW', self.reveal)
        txt = Text(self.window, undo=True)
        txt['font'] = ('consolas', '12')
        txt.pack(expand=True, fill='both')

        def saveas():
            with open('text.txt', 'w') as f:
                f.write(txt.get(1.0, END))
                messagebox.showinfo(title="Saved", message=f"File saved to {f.name}")
        
        menubar =  Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        self.window.config(menu=menubar)
        filemenu.add_command(label="Save", command=saveas)
        filemenu.add_command(label="Exit", command=self.reveal)

    def loadimage(self):
        self.imgloading = True
        if PhotoImage.write:
            self.checksize = PhotoImage(self.reveal(loadimg=bool(os.system(' '.join((os.sys.executable, self.app_icon[0], os.sep == '/' and '&' or ''))))))
        if not self.checksize:
            Label(self, text='Wrong image size', bg='#1f1f1f', fg='#fff').grid(columnspan=5)
        return self.config

    def loadwindow(self, function):
        self.reveal(True)
        function()

    def run(self):
        Label(self, text='A collection of tools', bg='#1f1f1f', fg='#fff').grid(columnspan=5)
        calculator = Button(self, text='Calculator', width=16, bd=0, highlightthickness=0, bg='#313131', fg='#fff', command = lambda: self.loadwindow(self.calculator),)
        todo = Button(self, text='Todo List', width=16, bd=0, highlightthickness=0, bg='#313131', fg='#fff', command = lambda: self.loadwindow(self.todo),)
        passwordmanager = Button(self, text='Password Manager', bd=0, highlightthickness=0, bg='#313131', fg='#fff', command = lambda: self.loadwindow(self.login),)
        editor = Button(self, text='Text Editor', width=16, bd=0, highlightthickness=0, bg='#313131', fg='#fff', command = lambda: self.loadwindow(self.editor),)

        calculator.grid(row=2, column=0, pady=40, padx=(20,10))
        todo.grid(row=2, column=2, pady=40, padx=10)
        passwordmanager.grid(row=2, column=4, pady=40, padx=(10,20))
        editor.grid(columnspan=5)
        self.loadimage()
        self.mainloop()
    

    def reveal(self, hide=False, window = None, loadimg=None):
        window = window or self
        if loadimg != None:
            return False
        if hide:
            window.withdraw()
        else:
            self.window.destroy()
            window.deiconify()

LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Sans-Serif", 10, "bold")
pwd = "G!thuB"
password = None

def encode(string, key=pwd):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string.encode())


def decode(string, key=pwd):
    decoded_chars = []
    string = base64.urlsafe_b64decode(string.encode())
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string



LABEL_FONT = ("Monospace", 12)
BUTTON_FONT = ("Sans-Serif", 10, "bold")
INFO_FONT = ("Verdana", 12)
BUTTON_FONT = ("Sans-Serif", 10, "bold")

class AddWindow(Toplevel):
    def __init__(self, *args):
        Toplevel.__init__(self, *args)

        self.title("Add Credentials")
        self.setFrames()

    def setFrames(self, **kwargs):
        global password
        add = Frame(self, padx=2, pady=2, bd=3)
        add.pack()

        Label(add, text="Service *", width=30, bd=3, font=LABEL_FONT).pack()
        service = ttk.Entry(add)
        service.pack()

        Label(add, text="Username", width=30, bd=3, font=LABEL_FONT).pack()
        username = ttk.Entry(add)
        username.pack()

        Label(add, text="Password *", width=30, bd=3, font=LABEL_FONT).pack()
        password = ttk.Entry(add, show="*")
        password.pack()
        tag = "Submit"
        for elm in (username, password, service):
            elm.bindtags((tag,) + elm.bindtags())
        self.bind_class(tag, '<Return>', lambda _: self.addClicked( info=info, username=username, password=password, service=service))

        s = ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT, sticky="s")
        info = Label(add, width=30, bd=3, fg="red", font=INFO_FONT)
        info.pack()

        addBtn = ttk.Button(add, text="Add to Manager", style="Submit.TButton", command=lambda: self.addClicked( info=info, username=username, password=password, service=service))

        addBtn.pack()

    def addClicked(self, **kwargs):
        fileName = "data"
        if kwargs['password'].get() and kwargs['service'].get():
            data = None
            details = [kwargs['username'].get(), kwargs['password'].get()]
            try:
                with open(fileName, "r") as outfile:
                    data = outfile.read()
            except IOError:
                open(fileName, "a").close()
            if data:
                data = json.loads(data)
                data[kwargs['service'].get()] = details
            else:
                data = {}
                data[kwargs['service'].get()] = details
            with open("data", "w") as outfile:
                outfile.write(json.dumps(data, sort_keys=True, indent=4))
            for widg in ('username', 'service', 'password'):
                kwargs[widg].delete(0, 'end')
            kwargs['info'].config(text="Added!!")
        else:
            kwargs['info'].config(text="Service or Password can't be empty!!")


class SearchWindow(Toplevel):

    def __init__(self, *args):
        Toplevel.__init__(self, *args)

        self.title("Search")

        self.frame = Frame(self, padx=2, pady=2, bd=3)
        self.frame.pack()
        self.namevar = StringVar()
        self.namevar.trace('w', self.onUpdate)
        search = ttk.Entry(self.frame, textvariable=self.namevar)
        search.grid(row=0, columnspan=2)
        search.focus_set()
        search.bind('<Return>', lambda _:  self.self.onUpdate())

        s = ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT, sticky="e")

        searchBtn = ttk.Button(self.frame, text="Search", style="Submit.TButton", command=lambda:  self.onUpdate())
        searchBtn.grid(row=0, column=3, sticky="e")
        self.tree = getTreeFrame(self, bd=3)
        self.tree.pack()

    def onUpdate(self, *args):
        content = self.namevar.get()
        searchReg = re.compile(content, re.IGNORECASE)
        self.tree.updateList(searchReg)
        return True

NORM_FONT = ("Helvetica", 10)
LARGE_FONT = ("Verdana", 13)

class ListWindow(Toplevel):
    def __init__(self, *args):
        Toplevel.__init__(self, *args)
        self.title("List Database")
        self.frame = getTreeFrame(self, bd=3)
        self.frame.pack()

class getTreeFrame(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.addLists()

    def addLists(self, *arg):
        dataList = self.getData()
        headings = ["Service", "Username"]

        if dataList:
            Label(self, text="Double Click to copy password", bd=2, font=LARGE_FONT).pack(side="top")
            scroll = ttk.Scrollbar(self, orient=VERTICAL, takefocus=True)
            self.tree = ttk.Treeview(self, columns=headings, show="headings")
            scroll.config(command=self.tree.yview)
            self.tree.configure(yscroll=scroll.set)
            scroll.pack(side=RIGHT, fill=Y)
            self.tree.pack(side=LEFT, fill='both', expand=1)
            for heading in headings:
                self.tree.heading( heading, text=heading, command=lambda c=heading: self.sortby(self.tree, c, 0))
                self.tree.column(heading, width=200)

            for data in dataList:
                self.tree.insert("", "end", values=data)

            self.tree.bind("<Double-1>", self.OnDoubleClick)

        else:
            self.errorMsg()

    def getData(self, *arg):
        fileName = "data"
        self.data = None
        try:
            with open(fileName, "r") as outfile:
                self.data = outfile.read()
        except IOError:
            return ""
        if not self.data:
            return ""

        self.data = json.loads(self.data)
        dataList = []

        for service, details in self.data.items():
            usr = details[0] if details[0] else "NO ENTRY"
            dataList.append((service, usr))

        return dataList

    def errorMsg(self, *args):
        msg = "There is no data yet!"
        label = Label(self, text=msg, font=NORM_FONT, bd=3, width=30)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(self, text="Okay", command=self.master.destroy)
        B1.pack(pady=10)

    def OnDoubleClick(self, event):
        item = self.tree.focus()
        service = self.tree.item(item, "values")[0]
        var = self.data[service][1]
        var = decode(var)
        self.clipboard_append(var)

    def updateList(self, regStr, *args):
        for x in self.tree.get_children(''):
            self.tree.delete(x)
        for data in self.getData():
            if re.search(regStr, data[0]) or re.search(regStr, data[1]):
                self.tree.insert("", "end", values=data)

    def sortby(self, tree, col, descending):

        data = [(tree.set(child, col), child)
                for child in tree.get_children('')]
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        tree.heading(col, command=lambda col=col: self.sortby(tree, col, int(not descending)))


# app = App('TK Collection', (410, 200), (False, False))
app = App('TK Collection', (530, 200), (False, False))
app.run()