"""
2023 © MySQLInterface Class , Sikrox Memer
Its An Example Of How To Make UI Using Python
Built in Module nter And Object Oriented
Programming.
"""

from Source.Config.MySQL import MySQL

from tkinter import *

class MySQLInterface(Tk):
    """
    MySQL Interface Class Object , Maker \n
    Its Class Can't Work Without The MySQL \n
    Object. it inherits its properties from \n
    nter Module. \n
    Syntax : \n
    App = MySQLInterface()
    """

    def __init__(self):
        super().__init__()
        self.title('Connect')
        self.geometry('512x312')
        self.resizable(False, False)
        self.blank = Label(
            text='',
            padx=60,
            pady=20).grid(column=0, row=0, padx=10, pady=10)
        # Localhost:
        self.Text = Label(
            text='MySQL.Python',
            font=('consolas', 25, 'bold'),
            padx=5,
            pady=5,
            foreground='black').grid(column=1, row=0, sticky=N)
        self.LocalHost = Label(
            text='Localhost :',
            font=('consolas', 15, 'bold')).grid(column=0, row=1)
        self.LocalHostEntry = Entry(
            self, width=35, font=('consolas', 10, 'bold'))
        self.LocalHostEntry.grid(column=1, row=1)
        # //
        self.T = Label(
            text='|My|',
            font=('consolas', 15, 'bold')).grid(column=2, row=1)
        self.T = Label(
            text='|S|',
            font=('consolas', 15, 'bold')).grid(column=2, row=2)
        self.T = Label(
            text='|Q|',
            font=('consolas', 15, 'bold')).grid(column=2, row=3)
        self.T = Label(
            text='|L|',
            font=('consolas', 15, 'bold')).grid(column=2, row=4)
        # //
        # UserName:
        self.Username = Label(
            text='Username :',
            font=('consolas', 15, 'bold')).grid(column=0, row=2)
        self.UsernameEntry = Entry(
            self, width=35, font=('consolas', 10, 'bold'))
        self.UsernameEntry.grid(column=1, row=2)
        # Password:

        self.Password = Label(
            text='Password :',
            font=('consolas', 15, 'bold')).grid(column=0, row=3)
        self.PasswordEntry = Entry(
            self, width=35, font=('consolas', 10, 'bold'))
        self.PasswordEntry.grid(column=1, row=3)
        # Database:

        self.Database = Label(
            text='Database :',
            font=('consolas', 15, 'bold'), padx=15).grid(column=0, row=4)
        self.DatabaseEntry = Entry(
            self, width=35, font=('consolas', 10, 'bold'))
        self.DatabaseEntry.grid(column=1, row=4)
        # ConnectButton:

        self.ConnectButton = Button(
            text='Connect',
            font=('consolas', 10, 'bold'),
            padx=30,
            pady=5, command=self.Connect_To_Database).grid(column=0, row=5, pady=35)
        # pass:

        self.blank = Label(text='', padx=0, pady=0).grid(column=1, row=5)
        # ExitButton:

        self.ExitButton = Button(
            text='Exit',
            font=('consolas', 10, 'bold'),
            padx=30,
            pady=5, command=exit).grid(column=2, row=5)

    def Connect_To_Database(self):
        List = [self.LocalHostEntry.get(), self.PasswordEntry.get(),
                self.UsernameEntry.get(), self.DatabaseEntry.get()]
        Object = MySQL(
            host=List[0],
            password=List[1],
            user=List[2],
            database=List[3])

        Execution = Toplevel()
        Execution.geometry('512x312')
        Execution.resizable(False, False)
        Execution.title('Cursor')

        Execution.Title = Label(Execution, text='Cursor:',
                                font=('consolas', 25, 'bold'), padx=5)
        Execution.Title.grid(column=0, row=0)

        Execution.Entry = Entry(Execution,
                            width=50)
        
        Execution.Entry.grid(column=0, row=1)

        Value = Execution.Entry.get()

        fun = lambda sql=Value : Object.Execute(sql)

        Execution.button = Button(Execution, text='Execute',
                                  command=fun, padx=25, pady=10)

        Execution.button.grid(column=0, row=2, padx=25, pady=25)
    pass
pass