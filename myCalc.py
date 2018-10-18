from tkinter import*
# import everything from module

def iCalc(source, side):
    storeObj = Frame(source, borderwidth = 1, bd= 4, bg='grey')
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button (source, side, text, command = None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 18')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')


        discplay = StringVar()
        Entry(self, relief=GROOVE, textvariable=discplay, justify='right',
              bd=5, bg="light grey").pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in(["CE"], ["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=discplay, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for char in NumBut:
                button(FunctionNum, LEFT, char, lambda storeObj=discplay, q=char: storeObj.set(storeObj.get() + q))




if __name__ == '__main__':
    app().mainloop()